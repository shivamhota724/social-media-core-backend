from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from sqlalchemy.orm import Session

from database import SessionLocal, get_db
from models import Post, User
from schemas import CreatePost, PostResponse, CreateUser, UserResponse, UserLogin, Token
from utils import hash, verify
from oauth2 import create_access_token, get_current_user

app = FastAPI()


@app.post("/users", response_model=UserResponse)
def create_user(
    user: CreateUser,
    db: Session = Depends(get_db)
):
    """
    Registers a new user profile.
    Encrypts passwords using bcrypt before saving to the database.
    """
    # 1. Safeguard against duplicate records
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail='email already exists'
        )
        
    # 2. Persist the entity with a cryptographically secure hash
    new_user = User(
        email = user.email,
        password = hash(user.password) 
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticates user identities.
    Validates form data and signs an insulated JWT access token.
    """
    user = db.query(User).filter(User.email == user_credentials.username).first()

    if user is None:
        raise HTTPException(
            status_code=403,
            detail="Invalid credentials"
        )

    # Verify against hashed database records to prevent plain-text breaches
    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=403,
            detail="Invalid credentials"
        )
        
    access_token = create_access_token(
        data={"user_id": user.id}
    )
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.post("/posts", response_model=PostResponse)
def create_post(
    post: CreatePost,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Creates a new post record securely attached to the active session owner.
    """
    new_post = Post(
        content = post.content,
        owner_id = current_user.id # Establishes the relationship constraint
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/posts", response_model=List[PostResponse])
def get_posts( 
    db: Session = Depends(get_db),
    limit: int = Query(default=10, le=100, description="Limit the number of posts returned"),
    skip: int = Query(default=0, ge=0, description="Number of posts to skip for pagination")
):
    """
    Fetches posts utilizing high-throughput windowing (Pagination).
    
    CRITICAL LESSON:
    Using db.query(Post).all() pulls the entire table into memory.
    If the system contains millions of rows, it will trigger an Out-of-Memory (OOM) crash.
    By chaining .limit() and .offset(), the database engine only fetches short, fast segments.
    """
    return db.query(Post).limit(limit).offset(skip).all()


@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(
    post_id: int,  
    db: Session = Depends(get_db)
):
    """
    Retrieves a single, specific post by its primary key id context.
    """
    post = db.query(Post).filter(Post.id == post_id).first() 

    if post is None:
        raise HTTPException(
            status_code=404,
            detail='Post not found'
        )
    return post


@app.delete("/posts/{post_id}")
def delete_post(
    post_id: int,  
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    """
    Deletes a target resource post file.
    Validates cross-user sandboxing parameters before mutation.
    """
    post = db.query(Post).filter(Post.id == post_id).first()
    
    if post is None:
        raise HTTPException(
            status_code=404,
            detail='Post not found'
        )
        
    # CRITICAL LESSON: Multi-user isolation layer checking.
    # Prevents authenticated user A from dropping records belonging to user B.
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to perform this action"
        )
        
    db.delete(post)
    db.commit()
    return {"message" : "Post deleted successfully"}


@app.put("/posts/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    post_update: CreatePost,  
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Mutates text properties inside a pre-existing post entity.
    Requires validated ownership strings before pushing database transactions.
    """
    post = db.query(Post).filter(Post.id == post_id).first()

    if post is None:
        raise HTTPException(
            status_code=404,
            detail='Post not found'
        )
        
    # Enforces same strict sandboxing protection rules as the DELETE routing logic
    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to perform this action"
        )
        
    post.content = post_update.content
    db.commit()
    db.refresh(post) # Injects the clean database updates back into the response body
    return post

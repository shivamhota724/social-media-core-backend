# social-media-core-backend (RESTful Backend Architecture)

A production-ready, containerized REST API backend engine for relational data manipulation and token-based authorization.

🌐 Live System Documentation: https://twitter-api-931t.onrender.com/docs

## 🏗️ Core Architecture & Highlights
* **Stack:** Python, FastAPI, SQLAlchemy ORM, and PostgreSQL/SQLite.
* **Security:** Bcrypt password hashing and JWT Token Authentication using OAuth2.
* **Authorization:** Ownership verification for updating and deleting posts.

## 🚀 Local System Initiation

1. Clone the repository and navigate into the project directory:
   ```bash
   git clone https://github.com
   cd social-media-core-backend
   ```
2. Create and activate a python virtual environment:
   * **macOS / Linux:**
     ```bash
     python -m venv venv && source venv/bin/activate
     ```
   * **Windows:**
     ```bash
     python -m venv venv && venv\Scripts\activate
     ```
3. Install dependencies and run the server:
   ```bash
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

## 🌐 API Endpoints

### Authentication

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/users` | Register a new user |
| **POST** | `/login` | Login and receive JWT token |

### Posts

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/posts` | Get all posts |
| **GET** | `/posts/{post_id}` | Get a single post |
| **POST** | `/posts` | Create a new post |
| **PUT** | `/posts/{post_id}` | Update a post |
| **DELETE** | `/posts/{post_id}` | Delete a post |

---
**Author:** Shivam Hota  
**GitHub Profile:** [shivamhota724](https://github.com/shivamhota724)

# social-media-core-backend (RESTful Backend Architecture)

A production-ready, containerized REST API backend engine optimized for low-latency relational data manipulation, token-based authorization, and secure multi-user sandboxing.

🌐 Live System Documentation: https://onrender.com

## 🏗️ Core Architecture & Engineering Highlights
* **Containerized Deployment Multi-Stack:** Orchestrated using Docker and Docker Compose to link an isolated Python runtime context with a separate PostgreSQL database instance.
* **Granular Session Security:** Stateful authorization flow leveraging OAuth2 password specifications paired with cryptographically signed JWT access tokens.
* **Data Layer Optimization & Windowing:** Relational architecture mapped through SQLAlchemy ORM, incorporating database indexing on foreign key lookups (`owner_id`) and high-throughput query pagination boundaries (`limit` and `skip` query bounds) to prevent table-scan resource exhaustion.
* **Fail-Safe Multi-User Access Control:** Secure middleware layer explicitly verifying post-ownership strings, ensuring resource mutations (PUT/DELETE) strictly restrict cross-user structural modifications.

## 🛠️ Tech Stack & Systems Architecture
* **Core Runtime:** Python 3.10+ / FastAPI / Uvicorn ASGI Server
* **Persistence Layer:** PostgreSQL / SQLAlchemy ORM
* **Security Layer:** Passlib (Bcrypt password hashing) / PyJWT / OAuth2 Password Bearer Flow
* **Infrastructure Containerization:** Docker / Docker Compose

## 🚀 Optimized Local System Initiation
1. Ensure Docker Desktop is active on your host system.
2. Clone the repository and navigate into the project directory:
   ```bash
   git clone https://github.com
   cd twitter_api
   ```
3. Initialize the multi-container database and server ecosystem:
   ```bash
   docker compose up --build
   ```
4. Access the auto-generated, interactive OpenAPI/Swagger interfaces at: `http://localhost:8000/docs`

## 📊 Database Schema Relationships
* **Users Table:** Handles core profiles with columns `id` (Primary Key), `email` (Unique String Index), and `password` (Hashed String Block).
* **Posts Table:** Handles structural records with columns `id` (Primary Key), `content` (String), and `owner_id` (Indexed Foreign Key tied to `users.id` with a cascading delete parameter).

## 🚀 Future Roadmap Implementation
* Database schema migrations tracking using Alembic.
* Automated continuous integration/deployment (CI/CD) pipelines using GitHub Actions.

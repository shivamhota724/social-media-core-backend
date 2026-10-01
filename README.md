# social-media-core-backend (RESTful Backend Architecture)

A production-ready, containerized REST API backend engine built with FastAPI, PostgreSQL, and Redis caching.

🌐 Live System Documentation: https://onrender.com

## 🏗️ Core Architecture & Engineering Highlights
* **Multi-Container Architecture:** Orchestrated using Docker and Docker Compose to cleanly isolate the Python FastAPI runtime, PostgreSQL database, and Redis cache memory systems.
* **Low-Latency In-Memory Caching:** Integrated a high-performance **Redis Caching** layer on high-frequency single post fetches (`GET /posts/{post_id}`) with a 60-second expiration policy to optimize performance and prevent database load.
* **Data Layer Optimization & Windowing:** Configured relational structures through SQLAlchemy ORM, incorporating explicit server-side **query pagination limits (`limit` and `skip`)** and indexing on high-frequency foreign keys (`owner_id`) to eliminate resource-intensive table scans.
* **Granular Session Security & Sandboxing:** Enforced strict multi-user sandboxing parameters leveraging cryptographically signed JWT tokens and OAuth2 Password Bearer flows, ensuring resource mutations (`PUT` / `DELETE`) are completely restricted to verified owners.

## 🛠️ Tech Stack & Dependencies
* **Core Runtime:** Python 3.10+ / FastAPI / Uvicorn ASGI Server
* **Storage & Caching:** PostgreSQL / SQLAlchemy ORM / Redis / fastapi-cache2
* **Security & Auth:** Passlib (Bcrypt hashing) / PyJWT / OAuth2 Password Flow
* **Container Infrastructure:** Docker / Docker Compose

## 🚀 Local System Initiation
1. Ensure Docker Desktop is active on your host system.
2. Clone the repository and navigate into the directory:
   ```bash
   git clone https://github.com
   cd social-media-core-backend
   ```
3. Initialize the multi-container environment:
   ```bash
   docker compose --env-file .env up --build
   ```
4. Access the interactive OpenAPI/Swagger interfaces at: `http://localhost:8000/docs`

## 🌐 Core API Mappings
* **Authentication:** `POST /users` (Register Profile), `POST /login` (Authenticate Credentials)
* **Posts Interface:** `GET /posts` (Paginated), `GET /posts/{post_id}` (Cached via Redis), `POST /posts`, `PUT /posts/{post_id}`, `DELETE /posts/{post_id}`

---
**Author:** Shivam Hota ([shivamhota724](https://github.com))

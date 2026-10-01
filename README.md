# social-media-core-backend (RESTful Architecture Engine)

A production-ready, containerized backend engine built using FastAPI, PostgreSQL, and Redis, structured for isolated development and automated verification.

## 🏗️ Core Highlights & Systems Engineering
* **Multi-Container Architecture:** Orchestrated via Docker and Docker Compose to completely isolate the FastAPI application server, PostgreSQL database, and Redis cache clusters.
* **Low-Latency In-Memory Caching:** Integrated a Redis memory cache on high-frequency single post fetches (`GET /posts/{post_id}`) with a 60-second expiration lifecycle to optimize throughput.
* **Query Window Constraints:** Server-side pagination parameters (`limit` and `skip`) built straight into the core SQLAlchemy ORM queries to protect system memory buffers from table scan exhaustion.
* **Automated Quality Gateways:** Configured an automated integration testing workspace running `pytest` directly inside the active application container layer.

## 🚀 Local System Initiation & Testing

1. Ensure Docker Desktop is active on your host machine.
2. Clone and navigate to the project directory:
   ```bash
   git clone https://github.com
   cd social-media-core-backend
   ```
3. Initialize the environment configuration variables inside your `.env` file at the root.
4. Launch the entire containerized stack:
   ```bash
   docker compose --env-file .env up --build
   ```
5. Open a second terminal window tab and execute the automated testing validation suite:
   ```bash
   docker compose exec api pytest test_main.py
   ```

---
**Author:** Shivam Hota ([shivamhota724](https://github.com))

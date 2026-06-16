# ahoy_crud_api

A CRUD REST API built with FastAPI, SQLAlchemy, and PostgreSQL. Built as part of the Ahoy AI/ML Internship program (Month 1 — Week 3 deliverable).

---

## Stack

- **FastAPI** — API framework
- **SQLAlchemy** — ORM
- **PostgreSQL** — database
- **passlib + bcrypt** — password hashing
- **python-dotenv** — environment variable management

---

## Prerequisites

Make sure you have the following installed before starting:

- Python 3.11+
- PostgreSQL 18 ([download here](https://www.postgresql.org/download/windows/))
- Git

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/atikyy/ahoy_crud_api.git
cd ahoy_crud_api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` appear at the start of your terminal prompt.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL

Open **SQL Shell (psql)** from the Start menu and run:

```sql
CREATE DATABASE ahoy_api;
```

Hit Enter through all the prompts (Server, Database, Port, Username) and enter your PostgreSQL password when asked.

### 5. Create your `.env` file

Create a file called `.env` in the root of the project (same level as `app/`):

```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/ahoy_api
```

Replace `yourpassword` with the password you set during PostgreSQL installation.

> ⚠️ The `.env` file is intentionally not included in this repo — it contains credentials. Every team member creates their own.

### 6. Run the API

```bash
uvicorn app.main:app --reload
```

The API will start at `http://localhost:8000`.

---

## Testing the API

Open your browser and go to:

```
http://localhost:8000/docs
```

FastAPI's auto-generated docs UI will show all available endpoints. You can test every endpoint directly from there.

---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `POST` | `/users` | Create a new user |
| `GET` | `/users` | Get all users |
| `GET` | `/users/{id}` | Get a user by ID |
| `PUT` | `/users/{id}` | Update a user |
| `DELETE` | `/users/{id}` | Delete a user |

---

## Project Structure

```
ahoy_crud_api/
    app/
        __init__.py
        main.py          # entry point
        database.py      # engine + session setup
        models.py        # SQLAlchemy ORM models
        schemas.py       # Pydantic schemas
        routers/
            __init__.py
            users.py     # user endpoints
    .env                 # your local credentials (not committed)
    .gitignore
    requirements.txt
    README.md
```

---

## Common Issues

**`psql` not recognized in terminal**
Add PostgreSQL to your PATH: `C:\Program Files\PostgreSQL\18\bin` then restart VS Code.

**`relation "users" does not exist`**
The table gets created automatically on first run via `Base.metadata.create_all()`. Make sure your `.env` is set up correctly and the `ahoy_api` database exists in PostgreSQL.

**bcrypt version error**
The `requirements.txt` pins `bcrypt==4.0.1` which is required for compatibility with `passlib`. Running `pip install -r requirements.txt` should handle this automatically.

**`DATABASE_URL` is None**
Your `.env` file is either missing or not in the project root. Make sure it sits at the same level as the `app/` folder.

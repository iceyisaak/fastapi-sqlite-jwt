# FastAPI + SQLite + JWT Authentication Boilerplate

Repo: https://github.com/iceyisaak/fastapi-sqlite-jwt

This project provides a clean, production-ready implementation of **JWT (JSON Web Token)** authentication using **FastAPI** and **SQLite**. It includes user registration, secure password hashing, login/token generation, and protected route access.

## 📁 Repository Structure

```text
.
├── backend/
│   ├── app.py          # Main application logic & API endpoints
│   └── database.db     # SQLite database (generated automatically)
├── requirements.txt    # Project dependencies
└── README.md

```

## 🚀 Features

* **FastAPI Framework**: High-performance, easy-to-use asynchronous API.
* **SQLite + SQLAlchemy**: Lightweight database with ORM for easy data handling.
* **JWT Authentication**: Secure stateless authentication using `python-jose`.
* **Bcrypt Password Hashing**: Secure password storage using `passlib`.
* **Automatic Docs**: Interactive Swagger UI available at `/docs`.

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/iceyisaak/fastapi-sqlite-jwt.git
cd fastapi-sqlite-jwt

```

### 2. Set up a Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

---

## 🏃 Running the Application

Navigate to the `backend` directory and start the server using Uvicorn:

```bash
cd backend
uvicorn app:app --reload

```

The server will start at `http://127.0.0.1:8000`.

---

## 📖 API Usage Guide

### Interactive Documentation

View the auto-generated documentation to test endpoints directly:

* **Swagger UI**: [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)
* **ReDoc**: [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

### Key Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| **POST** | `/users/` | Register a new user with username and password. |
| **POST** | `/token` | Exchange credentials for a JWT access token. |
| **GET** | `/users/me/` | Retrieve the current authenticated user's profile. |

### How to Authenticate

1. **Register**: Create a user via `POST /users/`.
2. **Login**: Send your credentials to `POST /token`. You will receive an `access_token`.
3. **Access Protected Routes**: In the Swagger UI, click the **Authorize** button and paste your token, or add the header manually to your requests:
`Authorization: Bearer <your_token>`

---

## 🔒 Security Notes

* **Secret Key**: In `app.py`, ensure you change the `SECRET_KEY` variable to a unique, random string for production.
* **Token Expiry**: The default expiration is set to 30 minutes. You can adjust this in the `ACCESS_TOKEN_EXPIRE_MINUTES` variable.


---
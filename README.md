# 📘 SkillBridge Attendance API

Backend API for a fictional state-level skilling programme **SkillBridge**, supporting role-based access control, JWT authentication, and attendance tracking.

---

# 🌐 Live API

```bash
https://attendance-api-10.onrender.com
https://attendance-api-10.onrender.com/docs
```

---

# 🚀 Tech Stack

* **Framework**: FastAPI
* **Database**: PostgreSQL (Neon)
* **ORM**: SQLAlchemy
* **Auth**: JWT (python-jose)
* **Deployment**: Render

---

# ⚙️ Local Setup

```bash
git clone https://github.com/prassu02/Attendance-api
cd Attendance-api

pip install -r requirements.txt

# create .env file
cp .env.example .env

uvicorn src.main:app --reload
```

---

# 🔐 Authentication

## 1. Signup

```bash
POST /auth/signup
```

```json
{
  "name": "John",
  "email": "john@test.com",
  "password": "123456",
  "role": "student"
}
```

---

## 2. Login

```bash
POST /auth/login
```

Returns JWT:

```json
{
  "access_token": "your_token",
  "token_type": "bearer"
}
```

---

# 🔑 JWT Structure

## Access Token (24h)

```json
{
  "user_id": 1,
  "role": "trainer",
  "iat": "...",
  "exp": "..."
}
```

---

## Monitoring Token (1h)

```json
{
  "user_id": 5,
  "role": "monitoring_officer",
  "scope": "monitoring",
  "exp": "..."
}
```

---

# 🛡️ Role-Based Access Control (RBAC)

Each endpoint validates role from JWT.

Example:

* Student → mark attendance
* Trainer → create sessions
* Institution → view batch summary
* Programme Manager → global summary
* Monitoring Officer → read-only access

Unauthorized access returns:

```json
403 Forbidden
```

---

# 📌 API Endpoints

## Auth

```bash
POST /auth/signup
POST /auth/login
POST /auth/monitoring-token
```

---

## Batches

```bash
POST /batches
POST /batches/{id}/invite
POST /batches/join
GET  /batches/{id}/summary
```

---

## Sessions

```bash
POST /sessions
GET  /sessions/{id}/attendance
```

---

## Attendance

```bash
POST /attendance/mark
```

---

## Programme

```bash
GET /institutions/{id}/summary
GET /programme/summary
```

---

## Monitoring (Read-only)

```bash
GET /monitoring/attendance
```

⚠️ Only accepts Monitoring Token
⚠️ POST → returns 405

---

# 🧪 Tests

Run tests:

```bash
pytest
```

### Covered Cases:

* ✅ Signup & login returns JWT
* ✅ Trainer creates session
* ✅ Student marks attendance
* ✅ Monitoring POST → 405
* ✅ No token → 401

---

# 🌱 Seed Data

Run:

```bash
python seed.py
```

Creates:

* 2 institutions
* 4 trainers
* 15 students
* 3 batches
* sessions + attendance

---

# 👤 Test Accounts

```bash
Student:
email: student@test.com
password: 123456

Trainer:
email: trainer@test.com
password: 123456

Institution:
email: institution@test.com
password: 123456

Programme Manager:
email: pm@test.com
password: 123456

Monitoring Officer:
email: monitor@test.com
password: 123456
```

---

# 🔑 Monitoring Token Flow

```bash
POST /auth/monitoring-token
```

```json
{
  "key": "SECRET_API_KEY"
}
```

* Requires Monitoring Officer JWT
* Returns short-lived token (1 hour)
* Used only for `/monitoring/*` endpoints

---

# ⚠️ Error Handling

* 422 → Validation errors
* 404 → Invalid IDs (batch/session)
* 403 → Unauthorized role access
* 401 → Missing/invalid token

---

# 🧠 Design Decisions

### 1. batch_trainers (Many-to-Many)

Allows multiple trainers per batch.

### 2. batch_invites

Token-based system for students to join batches.

### 3. Dual-token system

Monitoring Officer requires:

* Login JWT
* Additional scoped monitoring token

---

# 🔒 Security Notes

### Current Limitation:

* No token revocation

### Improvement:

* Use Redis blacklist for invalid tokens
* Add refresh tokens
* Rotate API keys periodically

---

# ✅ What’s Working

* ✔ Full authentication system
* ✔ Role-based access control
* ✔ Attendance tracking
* ✔ Monitoring token security
* ✔ Deployment (Render)

---

# ⚠️ What’s Incomplete

* No pagination
* No rate limiting
* Minimal logging

---

# 🚀 Future Improvements

* Add caching (Redis)
* Add analytics dashboard
* Add async DB optimization

---

# 📬 Contact

```bash
Name: Prasanna Kumar
Email: prasuprasanna8978@gmail.com
GitHub: https://github.com/prassu02
```



from src.database import Base, engine, SessionLocal
from src.models import User
from src.auth import hash_password

Base.metadata.create_all(bind=engine)

db = SessionLocal()

users = [
    User(email="student@test.com", password=hash_password("1234"), role="student"),
    User(email="trainer@test.com", password=hash_password("1234"), role="trainer"),
]

db.add_all(users)
db.commit()

print("Seeded")
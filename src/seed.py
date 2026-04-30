from .database import SessionLocal
from .models import User
from .auth import hash_password

db=SessionLocal()

roles=["student","trainer","institution","programme_manager","monitoring_officer"]
for i,r in enumerate(roles):
    db.add(User(name=r,email=f"{r}@test.com",
    password=hash_password("123"),role=r))

db.commit()
print("seed done")
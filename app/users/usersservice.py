from fastapi import Depends
from config.database import get_db

from .models import User
from sqlalchemy.orm import Session
from .schema import RegisterUser
from config.hashing import Hashing


class UserService:
    def get_user(email: str, db: Session = Depends(get_db)):
        return db.query(User).filter(User.email == email).first()

    def create_user(user: RegisterUser, db: Session = Depends(get_db)):
        db_user = User(
            name=user.name, email=user.email, password=Hashing.bcrypt(user.password)
        )

        db.add(db_user)
        db.commit()

        db.refresh(db_user)
        db_user.password = None

        return db_user

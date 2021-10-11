from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from .models import User
from .schema import RegisterUser
from .usersservice import UserService
from config.token import get_currentUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def createUser(user: RegisterUser, db: Session = Depends(get_db)):
    return UserService.create_user(user, db)


@router.get("/me")
def getMe(current_user: User = Depends(get_currentUser)):
    return current_user

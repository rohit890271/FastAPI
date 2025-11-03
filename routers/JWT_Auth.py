# routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
from jose import jwt, JWTError

import models, schemas
from database import get_db
from JWT_Token import hash_password, verify_password, create_access_token,SECRET_KEY,ALGORITHM

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Register user (signup)
@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # check existing username
    existing = db.query(models.User).filter(models.User.name == user.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")
    new_user = models.User(
        name=user.name,
        age=user.age,
        password=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Login -> returns JWT token (uses form data)
@router.post("/login", response_model=schemas.Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    # form_data.username, form_data.password
    user = db.query(models.User).filter(models.User.name == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token({"sub": user.name})
    return {"access_token": token, "token_type": "bearer"}

# Utility dependency to get current user
def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Protected example
@router.get("/protected")
def protected_route(token: str):
    user = get_current_user(token)
    return {"message": f"Hello {user}, you accessed a protected route!"}
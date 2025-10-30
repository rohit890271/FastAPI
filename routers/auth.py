from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

router = APIRouter(prefix="/auth", tags=["Authentication"])

security = HTTPBasic()

# Dummy user (normally you'd store this in your database)
USER_DB = {
    "rohit": "pass123"
}

@router.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "rohit")
    correct_password = secrets.compare_digest(credentials.password, USER_DB["rohit"])

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return {"message": f"Welcome {credentials.username}!"}

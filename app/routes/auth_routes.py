from fastapi import APIRouter, HTTPException, Depends
from app.models import User
from app.utils import hash_password, verify_password, create_jwt

router = APIRouter()

@router.post("/register")
def register(username: str, password: str, role: str = "user"):
    """
    Register a new user.

    Args:
    - username (str): The username for the new user.
    - password (str): The password for the new user.
    - role (str): The role for the new user. Defaults to "user".

    Raises:
    HTTPException: If the username already exists.

    Returns:
    dict: A dictionary containing a success message.
    """
    if User.objects(username=username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = hash_password(password)
    user = User(username=username, password=hashed_password, role=role)
    user.save()
    return {"message": "User registered successfully"}

@router.post("/login")
def login(username: str, password: str):
    """
    Login and obtain a JWT token.

    Args:
    - username (str): The username of the user.
    - password (str): The password of the user.

    Raises:
    HTTPException: If the credentials are invalid.

    Returns:
    dict: A dictionary containing a single key, "access_token", which is a JWT token.
    """
    user = User.objects(username=username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_jwt({"user_id": str(user.id), "role": user.role})
    return {"access_token": token}

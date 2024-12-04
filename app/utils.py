from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer
from app.models import User

SECRET_KEY = "coding-sphere-djbvbb-487"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """
    Hashes a given password using the configured hash algorithm.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """
    Verifies a given plaintext password against a hashed password.

    Args:
        plain_password (str): The plaintext password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: Whether the plaintext password matches the hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt(data: dict):
    """
    Creates a JSON Web Token containing the given data.

    Args:
        data (dict): The data to encode in the token.

    Returns:
        str: The JSON Web Token.
    """
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def decode_jwt(token: str):
    """
    Decodes a given JSON Web Token, returning the decoded payload.

    Args:
        token (str): The JSON Web Token to decode.

    Returns:
        dict: The decoded payload of the token.

    Raises:
        HTTPException: If the token is invalid or has been tampered with.
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def require_role(role: str):
    """
    A decorator that requires a given role to access an endpoint.

    Args:
        role (str): The role required to access the endpoint.

    Returns:
        Callable[[str], dict]: A decorator that takes an HTTP Bearer token and
            returns the decoded payload of the token if the role is valid,
            otherwise raises an HTTPException.

    Raises:
        HTTPException: If the role is invalid or the token is invalid.
    """
    def decorator(token: str = Security(HTTPBearer())):
        decoded_token = decode_jwt(token.credentials)
        if decoded_token.get("role") != role:
            raise HTTPException(status_code=403, detail="Access forbidden")
        return decoded_token
    return decorator
from datetime import datetime, timedelta
from jose import jwt, JWTError
import hashlib

from app.config.settings import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# -------------------------
# PASSWORD HASHING
# -------------------------

def hash_password(password: str):

    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(plain_password: str, hashed_password: str):

    return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password


# -------------------------
# TOKEN CREATION
# -------------------------

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


# -------------------------
# TOKEN VERIFICATION
# -------------------------

def verify_token(token: str):

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("user_id")

        return user_id

    except JWTError:

        return None
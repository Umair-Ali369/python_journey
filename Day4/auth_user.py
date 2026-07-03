from datetime import datetime, timedelta, timezone
import bcrypt
from warnings import deprecated
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from Models.db_models import UserDB

SECRET_KEY = "THEWorldIsMine369"
ALGORITHM  = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTS = 30

## password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
## token scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

## hash password
def hashPassword(password : str) -> str:
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    return hashed_bytes.decode('utf-8')


## verify password 
def verifyPassword(plain : str, hashed : str) -> bool:
     return bcrypt.checkpw(plain.encode('utf-8'), hashed.encode('utf-8'))

## create jwt token
def create_token(data : dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTS)
    to_encode.update({"exp" : int(expire.timestamp())})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

## get current user
def getCurrentUser(
    token : str = Depends(oauth2_scheme),
    db : Session = Depends(get_db)
):
    credential_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Invalid or expired Token",
        headers = {"WWW-Authenticate" : "Bearer"}
    )
    try:
        payload  = jwt.decode(token , SECRET_KEY, algorithms=[ALGORITHM])
        user_id : int = payload.get("user_id")
        if user_id is None:
            raise credential_exception
    except JWTError:
        raise credential_exception
    
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise credential_exception
    return user


import os
from datetime import timedelta, datetime
from http.client import HTTPException
from jose import JWTError, jwt
from passlib.context import CryptContext

from pythonProject.custormer.dto.response.TokenData import TokenData

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')  # HMAC SHA256
ACCESS_TOKEN_EXPIRE_MINUTES: int | None = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class JwtService:
    def __init__(self):
        self.secret_key = SECRET_KEY
        self.algorithm = ALGORITHM
        self.access_token_expire_minutes = ACCESS_TOKEN_EXPIRE_MINUTES

    # Xác thực password
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    # Tạo JWT token
    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    # Xác thực và giải mã JWT token
    def verify_token(self, token: str):
        credentials_exception = HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            username: str = payload.get("username")
            role: str = payload.get("role")
            if username is None or role is None:
                raise credentials_exception
            token_data = TokenData(username=username, role=role)
            return token_data
        except JWTError:
            raise credentials_exception

jwt_service = JwtService()
from passlib.context import CryptContext
from app.models.credential import find_one

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def login_controller(username: str, password: str):
	filter = { 'username': username }
	cred = find_one(filter)

	if not cred:
		return False
	if not verify_password(password, cred['password']):
		return False

	return cred
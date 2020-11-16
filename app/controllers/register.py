from datetime import datetime
from passlib.context import CryptContext
from app.models.user import insert_one, find_one
from app.models import credential

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_credential(body):
	hashed_pass = pwd_context.hash(body['password'])
	payload = {
		'username': body['username'],
		'password': hashed_pass,
		'is_admin': False
	}
	credential.insert_one(payload)

def register_controller(body):
	filter_check = { 'username': body['username'] }
	existing_user = find_one(filter_check)
	if existing_user:
		return False

	create_credential(body)
	del body['password']
	body['wallet'] = { 'balance': 0, 'points': 0 }
	body['cart'] = []
	body['wishlist'] = []
	body['coupons'] = []
	body['suggestions'] = []
	body['search_histories'] = []
	body['created_at'] = datetime.now()
	body['updated_at'] = datetime.now()
	body['is_deleted'] = False
	response = insert_one(body)
	if response.inserted_id:
		return {'message': 'User created!'}
	else:
		return False
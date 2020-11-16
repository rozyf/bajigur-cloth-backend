from app.models.coupon import insert_one, find_one

def create_coupon(body):
	filter_check = { 'code': body['code'] }
	existing_coupon = find_one(filter_check)
	if existing_coupon:
		return False

	response = insert_one(body)
	if response.inserted_id:
		return {'message': 'Coupon created!'}
	else:
		return False

def get_all_coupons(codes):
	return {}

def share_to_all(coupons):
	return True

def share_coupons(body):
	coupon_ids = body['coupon_codes']
	coupons = get_all_coupons(coupon_ids)
	response = share_to_all(coupons)
	if response:
		return { 'message': 'success share coupon_codes to all users' }

def share_coupons_to_user(body, user_id):
	return { 'message': f"success share coupons to {user_id}" }
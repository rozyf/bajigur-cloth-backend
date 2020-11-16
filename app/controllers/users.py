def get_product_suggestions(current_user):
	return { 'products': [] }

def get_product_discounts(current_user):
	return { 'products': [] }

def get_user_membership_level(current_user):
	return { 'username': current_user['username'], 'level': 1 }
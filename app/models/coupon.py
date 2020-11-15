from app.models import coupons_collection

def insert_one(coupon):
	result = coupons_collection.insert_one(coupon)
	return result

def insert_many(coupons):
	results = coupons_collection.insert_many(coupons)
	return results

def find(filter = {}, sort = ['created_at', -1], offset = 0, limit = 25):
	cursor = coupons_collection.find(filter).sort(sort[0], sort[1]).skip(offset).limit(limit)
	results = list(cursor)
	return results

def find_one(filter = {}):
	result = coupons_collection.find_one(filter)
	return result

def update_one(query, data):
	result = coupons_collection.update_one(query, data)
	return result

def update_many(query, data):
	results = coupons_collection.update_many(query, data)
	return results

def delete_one(query):
	result = coupons_collection.delete_one(query)
	return result

def delete_many(query):
	results = coupons_collection.delete_many(query)
	return results
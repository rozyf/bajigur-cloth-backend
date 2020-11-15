from app.models import orders_collection

def insert_one(order):
	result = orders_collection.insert_one(order)
	return result

def insert_many(orders):
	results = orders_collection.insert_many(orders)
	return results

def find(filter = {}, sort = ['created_at', -1], offset = 0, limit = 25):
	cursor = orders_collection.find(filter).sort(sort[0], sort[1]).skip(offset).limit(limit)
	results = list(cursor)
	return results

def find_one(filter = {}):
	result = orders_collection.find_one(filter)
	return result

def update_one(query, data):
	result = orders_collection.update_one(query, data)
	return result

def update_many(query, data):
	results = orders_collection.update_many(query, data)
	return results

def delete_one(query):
	result = orders_collection.delete_one(query)
	return result

def delete_many(query):
	results = orders_collection.delete_many(query)
	return results
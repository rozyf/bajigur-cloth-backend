from app.models import users_collection

def insert_one(user):
	result = users_collection.insert_one(user)
	return result

def insert_many(users):
	results = users_collection.insert_many(users)
	return results

def find(filter = {}, sort = ['_id', 1], offset = 0, limit = 25):
	cursor = users_collection.find(filter).sort(sort[0], sort[1]).skip(offset).limit(limit)
	results = list(cursor)
	return results

def find_one(filter = {}):
	result = users_collection.find_one(filter)
	return result

def update_one(query, data):
	result = users_collection.update_one(query, data)
	return result

def update_many(query, data):
	results = users_collection.update_many(query, data)
	return results

def delete_one(query):
	result = users_collection.delete_one(query)
	return result

def delete_many(query):
	results = users_collection.delete_many(query)
	return results
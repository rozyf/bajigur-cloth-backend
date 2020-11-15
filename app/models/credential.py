from app.models import credentials_collection

def insert_one(credential):
	result = credentials_collection.insert_one(credential)
	return result

def insert_many(credentials):
	results = credentials_collection.insert_many(credentials)
	return results

def find(filter = {}, sort = ['created_at', -1], offset = 0, limit = 25):
	cursor = credentials_collection.find(filter).sort(sort[0], sort[1]).skip(offset).limit(limit)
	results = list(cursor)
	return results

def find_one(filter = {}):
	result = credentials_collection.find_one(filter)
	return result

def update_one(query, data):
	result = credentials_collection.update_one(query, data)
	return result

def update_many(query, data):
	results = credentials_collection.update_many(query, data)
	return results

def delete_one(query):
	result = credentials_collection.delete_one(query)
	return result

def delete_many(query):
	results = credentials_collection.delete_many(query)
	return results
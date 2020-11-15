from app.models import items_collection

def insert_one(item):
	result = items_collection.insert_one(item)
	return result

def insert_many(items):
	results = items_collection.insert_many(items)
	return results

def find(filter = {}, sort = ['created_at', -1], offset = 0, limit = 25):
	cursor = items_collection.find(filter).sort(sort[0], sort[1]).skip(offset).limit(limit)
	results = list(cursor)
	return results

def find_one(filter = {}):
	result = items_collection.find_one(filter)
	return result

def update_one(query, data):
	result = items_collection.update_one(query, data)
	return result

def update_many(query, data):
	results = items_collection.update_many(query, data)
	return results

def delete_one(query):
	result = items_collection.delete_one(query)
	return result

def delete_many(query):
	results = items_collection.delete_many(query)
	return results
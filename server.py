from fastapi import FastAPI
from configs import title, api_description, tags_metadata, version
from configs.routes import routes

app = FastAPI(
	title = title,
	version = version,
	description = api_description,
	openapi_tags = tags_metadata
)

routes(app)

# from app.models import user
# from bson.objectid import ObjectId
# from datetime import datetime

# filter = {
# 	'_id': ObjectId('5fad701b6c4314ecef4af045')
# }
# users = user.find(filter)
# if users:
# 	print(users)
# else:
# 	print('users kosong')

# user = user.find_one(filter)
# if user:
# 	print(user)
# else:
# 	print('user kosong')

# current_time = datetime.now()

# updated_data = user.update_one(filter, { '$set': { 'updated_at': current_time } })
# print(updated_data.modified_count)


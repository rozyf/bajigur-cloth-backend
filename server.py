from fastapi import FastAPI
from configs import api_description, tags_metadata
from configs.routes import routes

app = FastAPI(
	title = 'Bajigur Cloth Backend API',
	description = api_description,
	openapi_tags = tags_metadata
)

routes(app)


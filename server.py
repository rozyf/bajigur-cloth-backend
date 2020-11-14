from fastapi import FastAPI
from configs.routes import routes

api_description = '<h3><strong>This is the API for Bajigur Cloth Backend Project. Go to <span style="color:red;">Highlight Feature Section</span> for the feature API (for tees.co.id coding test). Click Authorize button below and login using username "johndoe", and password "secret" for testing the API</strong></h3>'
tags_metadata = [
	{
		'name': 'LOGIN & REGISTER',
		'description': 'This section contains API for login to get token and register for new users'
	},
	{
		'name': 'HIGHLIGHT FEATURE',
		'description': '  <h3><p style="color:red;" ><b><strong>*</strong></b>Task for <strong><i>tees.co.id<i><strong><p></h3>'
	}
]


app = FastAPI(
	title = 'Bajigur Cloth Backend API',
	description = api_description,
	openapi_tags = tags_metadata
)

routes(app)


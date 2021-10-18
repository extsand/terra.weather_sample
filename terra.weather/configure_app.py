import os
#Grab all config variables from .env file
# more https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
from decouple import config

TEST_VAR = 'You can use configuration from .env'

print(f"Env is: {os.getenv('ENV_OS')}")

if os.getenv('ENV_IS'):
	print(f"OS environment is enable. Loading.")
	API_KEY_OWM = os.getenv('APIKEY_OWM')
	APP_PORT = os.getenv('APP_PORT')

	DB_MONGO_USER = os.getenv('DB_MONGO_USER')
	DB_MONGO_PASSWORD = os.getenv('DB_MONGO_PASSWORD')
	DB_MONGO_HOST = os.getenv('DB_MONGO_HOST')
	DB_MONGO_PORT = os.getenv('DB_MONGO_PORT')
else:
	print(f"OS environment is Disabled. Loading data from .env file.")
	API_KEY_OWM = config('APIKEY_OWM')
	APP_PORT = config('APP_PORT')

	DB_MONGO_USER = config('DB_MONGO_USER')
	DB_MONGO_PASSWORD = config('DB_MONGO_PASSWORD')
	DB_MONGO_HOST = config('DB_MONGO_HOST')
	DB_MONGO_PORT = config('DB_MONGO_PORT')
	DB_STORAGE = config('DB_STORAGE')

	ME_CONFIG_MONGODB_SERVER = config('ME_CONFIG_MONGODB_SERVER')
	ME_PORT = config('ME_PORT')



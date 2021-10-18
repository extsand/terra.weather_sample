#Example
# How to use json file for store and usage in python app

import json

with open('_terra.weather_credentials.json') as config_file:
    config = json.load(config_file)


class Config:
    APIKEY_OWM = config.get("APIKEY_OWM")

    DB_MONGO_USER = config.get("DB_MONGO_USER")
    DB_MONGO_PASSWORD = config.get("DB_MONGO_PASSWORD")
    DB_MONGO_HOST = config.get("DB_MONGO_HOST")
    DB_MONGO_PORT = config.get("DB_MONGO_PORT")

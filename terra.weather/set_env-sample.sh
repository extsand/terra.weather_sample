#!/bin/bash

echo 'Add Environment Variables'
#configure
export ENV_OS=True
#app
export APIKEY_OWM=sample_config
export APP_PORT=sample_config

#mongodb
export DB_MONGO_USER=sample_config
export DB_MONGO_PASSWORD=sample_config+1
export DB_MONGO_PORT=sample_config
export DB_STORAGE=./sample_config    

#local server
# export DB_MONGO_HOST=sample_config

#global server
DB_MONGO_HOST=sample_config


#mongo-express db handler
export ME_CONFIG_MONGODB_SERVER=sample_config
export ME_PORT=sample_config

#debug-mod
export SET_DATA_TO_DB=1


env | grep 'DB_\|APP_\|API'
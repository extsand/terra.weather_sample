import pymongo
import json
import configure_app
import ssl

#file for insert
path_to_file_fl = "../static/city.list.json"
path_to_file_short = "../static/ua_cities_list"
# offline_data = '../db_local/local_cities'
#authorization

client = pymongo.MongoClient(f"{configure_app.DB_MONGO_HOST}:{configure_app.DB_MONGO_PORT}",
                             ssl_cert_reqs=ssl.CERT_NONE,
                             username=configure_app.DB_MONGO_USER,
                             password=configure_app.DB_MONGO_PASSWORD,
                             authMechanism='SCRAM-SHA-256',

                             )




# db_def = client.get_default_database()
# print(db_def)

#Create db
db = client['terra_weather']
collect = db['cities_list']


# def getLocalData(localData):
#     f = open(localData, "r", encoding="utf-8")
#     data = json.loads(f.read())
#     for i in data:
#         offline_storage.update(i)
#         print(f"INSERT: {i}")
#     f.close()


# try:
#     for item in collect.find():
#         print(item["name"])
# except pymongo.errors.ServerSelectionTimeoutError:
#     print('DataBase offline, load reserve data')

# getLocalData(offline_data)
#
# print(offline_storage)


#Show all items
# for item in collect.find():
#   print(item["name"])

def getAllInfoFromDB(collect=collect):
    city_list = []
    for item in collect.find():
        buffer = {
            "id": item['id'],
            "name": item['name'],
            "country": item['country'],
            "lon": item['coord']['lon'],
            "lat": item['coord']['lat']
        }
        city_list.append(buffer)

    return city_list

# getAllInfoFromDB(collect)



def insertDataFromFile(json_fileName,db_collect):
    f = open(json_fileName, "r", encoding="utf-8")
    data = json.loads(f.read())
    for i in data:
        db_collect.insert_one(i)
        print(f"INSERT: {i}")
    f.close()

#you will use it once!
#on use .env value
# insertDataFromFile(path_to_file_fl, collect)


def findCity(name="Kyiv"):
    query = {"name": str(name)}
    document = collect.find(query)
    for x in document:
        print(f"I found: {x}")



def getAllCitiesName():
    city_list = []
    for city_name in collect.find():
        # city_name['name']
        item = city_name["name"]
        city_list.append(item)
    return city_list

def getCityNameFromFirstLetter(letter='Ky'):
    city_list = []
    query = {"name": {"$regex": f"^{letter}"}}
    document = collect.find(query)
    for x in document:
        # print(x['name'])
        city_list.append(x['name'])
    return city_list

def getCityFromCountry(country='UA'):
    city_list = []
    query = {"country": country}
    document = collect.find(query)
    for i in document:
        city_list.append(i["name"])
    city_list.sort()
    return city_list



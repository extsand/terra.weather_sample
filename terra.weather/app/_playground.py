import json
city_list = []
city = ''
id = 0

f = open('../static/city.list.json', 'r', encoding='utf-8')
cities = json.load(f)


# print(cities)
# for i in cities:
#     city = f"id: '{i['id']}', name: {i['name']}, country: {i['country']}"
#     # city_list.append(city)
for i in cities:
    city = f"id: '{i['id']}', name: {i['name']}, country: {i['country']}"
    city_list.append(city)

f.close()

# print(city_list)
# city_json = json.dumps(city_list)
# nf = open('file.json', 'x')
# nf.write(city_json)
# nf.close()
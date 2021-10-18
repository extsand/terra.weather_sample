# https://github.com/csparpa/pyowm
#More about storm
# https://neftegaz.ru/tech-library/suda-neftegazovye-i-morskoe-oborudovanie-dlya-bureniya/141644-klassifikatsiya-sily-vetra-volneniya-na-more-i-vidimosti-na-more/
import configure_app
from pyowm import OWM

# print(configure_app.TEST_VAR)


APIKEY_OWM = configure_app.API_KEY_OWM
owm = OWM(APIKEY_OWM)
manager = owm.weather_manager()


#forecast True/False
# forecast = manager.forecast_at_place('London', 'daily')
# answer = forecast.will_be_clear_at(timestamps.tomorrow())


def getWeather(city='Kiev'):
    data = {}
    observ = manager.weather_at_place(city)
    weather = observ.weather

    detailed_status = weather.detailed_status        # 'clouds'
    wind = weather.wind()                            # {'speed': 4.6, 'deg': 330}
    humidity = weather.humidity                      # 87
    temperature = weather.temperature('celsius')     # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    rain = weather.rain                              # {}
    heat_index = weather.heat_index                  # None
    clouds = weather.clouds

    data['city'] = city
    data['temp'] = temperature['temp']
    data['wind'] = wind
    data['clouds'] = clouds
    data['rain'] = rain

    #debug info
    #rain = {
    #     "1h": 0.56
    # }

    if rain != '':
        size = len(rain)
        if size:
            data['rain'] = rain[f"{size}h"]
        else:
            data['rain'] = 'No'

    return data

print(f"Weather api: {getWeather()}")



# Debug info ==================
# data = getWeather()
# print(data['rain'])

# city = getWeather('Kyiv')
#
# c_ky = {
#     'city': 'Kiev',
#     'temp': 11.81,
#     'wind': {
#         'speed': 0,
#         'deg': 0
#     },
#     'rain': {
#         '1h': '0.25',
#         # '2h': '1.23'
#     },
#     'clouds': 0
# }
#
# if c_ky['rain']:
#     size = len(c_ky['rain'])
#     if size:
#
#         print(c_ky['rain'][f"{size}h"])
# else:
#     print('Empty')




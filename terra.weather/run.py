from flask import Flask, request
from flask import render_template


from app.weather_a import getWeather
from app.time_a import getTime
from app.mongodb_a import getCityFromCountry, getAllInfoFromDB




docker_host = "0.0.0.0"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    date = getTime()
    city = getWeather('Kiev')
    # city_names = getAllCitiesName()
    # city_names = getCityNameFromFirstLetter()
    city_names = getCityFromCountry('UA')
    if request.method == 'POST':
        city = getWeather(request.form['city'])
        return render_template('home.html',
                               city=city,
                               date=date,
                               city_names=city_names
                               )

    return render_template('home.html',
                           city=city,
                           date=date,
                           city_names=city_names)

def modifyData_addCoordLink(data):
    # https://www.google.com/maps/search/45.3833347,32.5311403
    # link = f"https://www.google.com/maps/search/{lat},{lon}"
    def addCoord(lat, lon):
        link = f"https://www.google.com/maps/search/{lat},{lon}"
        return link
    modify_data = []
    for item in data:
        buffer = {
            "id": item['id'],
            "name": item['name'],
            "country": item['country'],
            "lat": item['lat'],
            "lon": item['lon'],
            "link": addCoord(item['lat'], item['lon'])
        }
        modify_data.append(buffer)
    return modify_data


@app.route('/cities')
def cities():
    data = getAllInfoFromDB()
    data_with_link = modifyData_addCoordLink(data)
    return render_template('cities.html',
                           data=data_with_link)


@app.route('/404', methods=['GET', 'POST'])
def in_progress():

    return render_template('in-progress.html')


if __name__ == '__main__':
    app.run(host=docker_host)

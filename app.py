import requests
from os import environ
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

""" Return weather data from end-point """
def get_weather_data(city):
    url = environ.get('END_POINT_UNITS')
    res = requests.get(url.format(city)).json()
    return res

""" Return render with context (weather_data) """
@app.route('/weather', methods=['GET', 'POST'])
def index():
    city = request.form.get('city')
    if city == '':
        city = "Medellin"
    res = get_weather_data(city)
    print(res['cod'])
    if res['cod'] == '404':
        city = "Medellin"
        res = get_weather_data('Medellin')
        
    weather = {
        'city' : city,
        'temperature' : res['main']['temp'],
        'description' : res['weather'][0]['description'],
        'icon' : res['weather'][0]['icon'],
    }
 
    weather_data = []
    weather_data.append(weather)

    return render_template('/index.html', weather_data=weather_data, response=res)
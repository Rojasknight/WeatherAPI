import requests
from os import environ
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True


""" Return render with context (weather_data) """

@app.route('/weather', methods=['GET', 'POST'])
def index():
    url = environ.get('END_POINT_UNITS')
    city = request.form.get('city')
    if city == '':
        city = "Medellin"
    res = requests.get(url.format(city)).json()
    
    weather = {
        'city' : city,
        'temperature' : res['main']['temp'],
        'description' : res['weather'][0]['description'],
        'icon' : res['weather'][0]['icon'],
    }
 
    weather_data = []
    weather_data.append(weather)

    return render_template('/index.html')
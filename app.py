import requests
from os import environ
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

""" Return render with context (weather_data) """
@app.route('/weather')
def index():
    url = environ.get('END_POINT_UNITS')
    city = request.form.get('city')

    return render_template('/index.html')
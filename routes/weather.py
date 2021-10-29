from flask import request, render_template, jsonify
from app import app
from config import Config
import requests


@app.route('/weather')
def weather():
    city = request.args.get('city')
    response = requests.get(
        Config.WEATHER_API_URL + "?key=" + Config.WEATHER_API_KEY + "&q=" + city + "&aqi=yes"
    )
    return response.json()


@app.route('/weather-for-cities')
def weather_for_cities():
    big_response = {}
    cities = request.args.get('cities')
    for city in cities.split(' '):
        response = requests.get(
            Config.WEATHER_API_URL + "?key=" + Config.WEATHER_API_KEY + "&q=" + city + "&aqi=yes"
        )
        big_response[city] = response.json()
    return jsonify(big_response)


@app.route('/get-your-weather')
def yourWeather():
    return render_template('weather.html')

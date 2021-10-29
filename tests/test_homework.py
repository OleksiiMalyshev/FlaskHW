from unittest import TestCase
from app import app
import json


class TestApp(TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_weather_1(self):
        response = self.client.get("/weather?city=Kiev")
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json['location']['name'], 'Kiev')

    def test_weather_2(self):
        response = self.client.get("/weather-for-cities?cities=Kiev%20Lviv")
        self.assertEqual(isinstance(response.json,dict),True)
        self.assertEqual(response.status_code, 200)

    def test_weather_3(self):
        response = self.client.get("/get-your-weather")
        self.assertEqual(response.status_code, 200)
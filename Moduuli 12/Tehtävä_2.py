import json
import requests
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_key = "23f0783bb262c26c76ac51ca05024b57"
CITY = input("Hae kaupunking lämpötila: ")

def kelvin_celsiukseksi(kelvin):
    celsius = kelvin - 273.15
    return celsius

url = BASE_URL + "appid=" + API_key + "&q=" + CITY

response = requests.get(url).json()

lämpötila_kelvin = response["main"]["temp"]
säätila = response["weather"][0]["main"]
celsius = kelvin_celsiukseksi(lämpötila_kelvin)

print(f"Lämpötila paikassa {CITY} on: {celsius:.2f}°C ja säätila on '{säätila}'.")
#print(json.dumps(response, indent=2))
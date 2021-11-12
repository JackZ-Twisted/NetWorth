import inspect
import nordigen
from nordigen import Client
import os
import requests


def Get_AccessTokens(URL_TOKEN, SECRET_ID, SECRET_KEY):
    Data = {"secret_id": SECRET_ID, "secret_key": SECRET_KEY}
    response = requests.post(URL_TOKEN, data=Data)
    ACCESS_TOKEN = response.json()['access']
    REFRESH_TOKEN = response.json()['refresh']
    return ACCESS_TOKEN, REFRESH_TOKEN

#Access token parameters
URL_TOKEN = "https://ob.nordigen.com/api/v2/token/new/"
SECRET_ID = "3dfedbda-2037-4d5e-9546-cea9fa86185b"
SECRET_KEY = "0861c2c608fd35c1d7aa3d6a5d1dcaf2c3bf07fc3e6fd9e06793a1284e3a3ad25c01c28e190da9113098608fad17e6ae7ea6540362cf102f2a6a4da35092152e"

ACCESS_TOKEN, REFRESH_TOKEN = Get_AccessTokens(URL_TOKEN, SECRET_ID, SECRET_KEY)

URL_AUTH = "https://ob.nordigen.com/api/v2/institutions/?country=gb"
headers = {'Authorization' : f'Bearer {ACCESS_TOKEN}'}

response = requests.get(URL_AUTH, headers=headers)

print(response.json())
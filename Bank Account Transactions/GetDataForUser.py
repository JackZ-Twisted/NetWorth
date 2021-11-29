from AddAccount import AddUser
import requests
import json
import os

def get_accesstoken():
    SECRET_ID = "3dfedbda-2037-4d5e-9546-cea9fa86185b"
    SECRET_KEY = "0861c2c608fd35c1d7aa3d6a5d1dcaf2c3bf07fc3e6fd9e06793a1284e3a3ad25c01c28e190da9113098608fad17e6ae7ea6540362cf102f2a6a4da35092152e"
    Data = {"secret_id": SECRET_ID, "secret_key": SECRET_KEY}

    response = requests.post("https://ob.nordigen.com/api/v2/token/new/", data=Data).json()
    return response['access'], response['refresh']

def get_data(UserId, AUTH):
    with open("Account_Ids.txt", "r") as file:
        for line in file:
            if line == '\n':
                pass
            else:
                if line.split()[0] == f"{UserId}":
                    Account_ids = line.split()[2]
    #needs to work for multiple accounts with one user
    response = requests.get(f"https://ob.nordigen.com/api/v2/accounts/{Account_ids}/transactions/",
                            headers=AUTH).json()
    json_object = json.dumps(response, indent=5)

    with open(os.path.join(r'C:\Users\Jack\Documents\GitHub\NetWorth\Bank Account Transactions\Formatting\User Transaction Data',f"{UserId}.json"), "w") as outfile:
        outfile.write(json_object)




ACCESS_TOKEN, REFRESH_TOKEN = get_accesstoken()
AUTH = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
UserID = "Testid_00000009"

get_data(UserID, AUTH)
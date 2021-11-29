from AddAccount import AddUser
import requests


def get_accesstoken():
    SECRET_ID = "3dfedbda-2037-4d5e-9546-cea9fa86185b"
    SECRET_KEY = "0861c2c608fd35c1d7aa3d6a5d1dcaf2c3bf07fc3e6fd9e06793a1284e3a3ad25c01c28e190da9113098608fad17e6ae7ea6540362cf102f2a6a4da35092152e"
    Data = {"secret_id": SECRET_ID, "secret_key": SECRET_KEY}

    response = requests.post("https://ob.nordigen.com/api/v2/token/new/", data=Data).json()
    return response['access'], response['refresh']


def Getall_AccountIds(AUTH):
    with open("User_Ids.txt", "r") as file:
        for line in file:
            if len(line) != 1:
                Requisition_id = line.split()[1]
                response = requests.get(
                    f"https://ob.nordigen.com/api/v2/requisitions/{Requisition_id}/",headers=AUTH
                ).json()
                ACCOUNT_IDS = response['accounts']
                ACCOUNT_IDS = ",".join(ACCOUNT_IDS)
                Newline = " ".join([line.rstrip("\n"), ACCOUNT_IDS])

                with open("Account_ids.txt", "a") as file:
                    file.write(f"{Newline}\n")
    #print(file_lines)




ACCESS_TOKEN, REFRESH_TOKEN = get_accesstoken()
AUTH = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

Getall_AccountIds(AUTH)
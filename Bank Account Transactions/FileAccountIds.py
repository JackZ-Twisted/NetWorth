import requests


# This function gets the access token from the API to create an authentication code, so we can proceed through the
# API steps.
def get_accesstoken():
    secret_id = "3dfedbda-2037-4d5e-9546-cea9fa86185b"
    secret_key = "0861c2c608fd35c1d7aa3d6a5d1dcaf2c3bf07fc3e6fd9e06793a1284e3a3ad25c01c28e190da9113098608fad17e6" \
                 "ae7ea6540362cf102f2a6a4da35092152e"

    data = {"secret_id": secret_id, "secret_key": secret_key}
    response = requests.post("https://ob.nordigen.com/api/v2/token/new/", data=data).json()
    return response['access'], response['refresh']


def getall_accountids(auth):
    with open("User_Ids.txt", "r") as file:
        for line in file:
            if len(line) != 1:
                requisition_id = line.split()[1]
                response = requests.get(
                    f"https://ob.nordigen.com/api/v2/requisitions/{requisition_id}/", headers=auth
                ).json()
                account_ids = response['accounts']
                account_ids = ",".join(account_ids)
                newline = " ".join([line.rstrip("\n"), account_ids])

                with open("Account_ids.txt", "a"):
                    file.write(f"{newline}\n")


ACCESS_TOKEN, REFRESH_TOKEN = get_accesstoken()
AUTH = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

getall_accountids(AUTH)

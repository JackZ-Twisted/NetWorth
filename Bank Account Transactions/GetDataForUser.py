import requests
import json
import os


# This function gets the access token from the API to create an authentication code, so we can proceed through the
# API steps.
def get_accesstoken():
    secret_id = "3dfedbda-2037-4d5e-9546-cea9fa86185b"
    secret_key = "0861c2c608fd35c1d7aa3d6a5d1dcaf2c3bf07fc3e6fd9e06793a1284e3a3ad25c01c28e190da9113098608fad17e6" \
                 "ae7ea6540362cf102f2a6a4da35092152e"

    data = {"secret_id": secret_id, "secret_key": secret_key}
    response = requests.post("https://ob.nordigen.com/api/v2/token/new/", data=data).json()
    return response['access'], response['refresh']


def get_data(userid, auth):
    # Note: This should provide error for unknown user id
    # This finds the line that contains the userid entered and gets the respective account id on that line
    with open("Account_Ids.txt", "r") as file:
        for line in file:
            if line == '\n':
                pass
            else:
                if line.split()[0] == f"{userid}":
                    account_ids = line.split()[2]

    # Note: Needs to work for multiple accounts with one user
    # This gets the transaction,Balance and Details data (Json file) from the given user id and stores it in a file,
    # in the location specified by os.path.join
    response_transac = requests.get(f"https://ob.nordigen.com/api/v2/accounts/{account_ids}/transactions/",
                                    headers=auth
                                    ).json()
    response_balances = requests.get(f"https://ob.nordigen.com/api/v2/accounts/{account_ids}/balances/",
                                    headers=auth
                                    ).json()
    response_details = requests.get(f"https://ob.nordigen.com/api/v2/accounts/{account_ids}/details/",
                                    headers=auth
                                    ).json()

    json_object_transac = json.dumps(response_transac, indent=5)
    json_object_balances = json.dumps(response_balances, indent=2)
    json_object_details = json.dumps(response_details, indent=5)

    with open(os.path.join(
            r'C:\Users\Jack\Documents\GitHub\NetWorth\Bank Account Transactions\Formatting\User Transaction Data',
            f"{userid}_Transactions.json"), "w") as outfile:
        outfile.write(json_object_transac)
    with open(os.path.join(
            r'C:\Users\Jack\Documents\GitHub\NetWorth\Bank Account Transactions\Formatting\User Transaction Data',
            f"{userid}_Balances.json"), "w") as outfile:
        outfile.write(json_object_balances)
    with open(os.path.join(
            r'C:\Users\Jack\Documents\GitHub\NetWorth\Bank Account Transactions\Formatting\User Transaction Data',
            f"{userid}_Details.json"), "w") as outfile:
        outfile.write(json_object_details)


# Example use of function
ACCESS_TOKEN, REFRESH_TOKEN = get_accesstoken()
AUTH = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
UserID = "Testid_00000011"

get_data(UserID, AUTH)

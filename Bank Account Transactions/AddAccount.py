import requests
import webbrowser
from GenerateUserID import Unique_id, Add_Entry
import contextlib

import os


class AddUser:
    def __init__(self, country_code, bank):
        self.Country_code = country_code
        self.Bank = bank
        self.ACCESS_TOKEN, self.REFRESH_TOKEN = self.get_accesstoken()
        self.AUTH = {'Authorization': f'Bearer {self.ACCESS_TOKEN}'}
        self.INSTITUTION_ID = self.get_institution()
        self.REQUISITION_ID = self.get_link()

    def get_accesstoken(self):
        SECRET_ID = "3dfedbda-2037-4d5e-9546-cea9fa86185b"
        SECRET_KEY = "0861c2c608fd35c1d7aa3d6a5d1dcaf2c3bf07fc3e6fd9e06793a1284e3a3ad25c01c28e190da9113098608fad17e6ae7ea6540362cf102f2a6a4da35092152e"
        Data = {"secret_id": SECRET_ID, "secret_key": SECRET_KEY}

        response = requests.post("https://ob.nordigen.com/api/v2/token/new/", data=Data).json()
        return response['access'], response['refresh']

    def get_institution(self):
        response = requests.get(f"https://ob.nordigen.com/api/v2/institutions/?country={self.Country_code}", headers = self.AUTH).json()

        bankexists = False
        for bank in response:
            if bank['name'] == self.Bank:
                return bank['id']
        if not(bankexists):
            print("Incorrect institution name, see the documentation!")

    def get_link(self):
        #change redirect to web application home URL, when developed
        Id_Created = False
        Id = 0
        while not Id_Created:
            try:
                User_id = Unique_id(Id)
                Data = {"redirect": "https://www.youtube.com/", "institution_id":f"{self.INSTITUTION_ID}", "reference": f"{User_id}", "user_language": "EN"}
                response = requests.post("https://ob.nordigen.com/api/v2/requisitions/", headers=self.AUTH, data=Data).json()
                Add_Entry(User_id, response['id'])
                Requisition_id = response['id']
                Id_Created = True
            except KeyError:
                Id += 1
        print(f'User Id: {User_id} created, with Requisition Id: {Requisition_id}')
        webbrowser.open(response['link'])
        return response['id']

    def store_accountids(self):
        response = requests.get(f"https://ob.nordigen.com/api/v2/requisitions/{self.REQUISITION_ID}/",
                                headers=self.AUTH).json()

        ACCOUNT_IDS = response['accounts']
        ACCOUNT_IDS = ",".join(ACCOUNT_IDS)
        with open("Account_Ids.txt", "w+") as file:
            file.write(f"\n{ACCOUNT_IDS}")
        return response['accounts']


# def get_data(Userid):
#     ACCESS_TOKEN, REFRESH_TOKEN = AddUser().get_accounttoken()
#     AUTH = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
#
#
#     response = requests.get(f"https://ob.nordigen.com/api/v2/accounts/{ACCOUNT_IDS}/transactions/",
#                             headers=AUTH).json()
#     print(response)

def main():
    Person = AddUser("gb", "National Westminster Bank")

if __name__ == '__main__':
    main()






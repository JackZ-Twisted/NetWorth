import requests
import webbrowser
from GenerateUserID import unique_id, add_entry


class AddUser:
    def __init__(self, country_code, bank):
        # Initial variables needed to initiate class, the user has to type in the country code and exact name of their
        # bank
        self.Country_code = country_code
        self.Bank = bank

        # Executes each function, which act as each API step in the process
        self.ACCESS_TOKEN, self.REFRESH_TOKEN = self.get_accesstoken()
        self.AUTH = {'Authorization': f'Bearer {self.ACCESS_TOKEN}'}
        self.INSTITUTION_ID = self.get_institution()
        self.AGREEMENT_ID = self.user_agreement()
        self.get_link()

    # This function gets the access token from the API to create an authentication code, so we can proceed through the
    # API steps.
    def get_accesstoken(self):
        # These secrets come from Jacks Nordigen account, they are used to create an "Access Token"
        secret_id = "3dfedbda-2037-4d5e-9546-cea9fa86185b"
        secret_key = "0861c2c608fd35c1d7aa3d6a5d1dcaf2c3bf07fc3e6fd9e06793a1284e3a3ad25c01c28e190da9113098608fad17e6" \
                     "ae7ea6540362cf102f2a6a4da35092152e"

        # Returns the "Access Token" AND "Refresh Token", the access token is used to create authentication so that
        # you can access each step in the API process, the refresh token I am unsure of.
        data = {"secret_id": secret_id, "secret_key": secret_key}
        response = requests.post("https://ob.nordigen.com/api/v2/token/new/", data=data).json()
        return response['access'], response['refresh']

    # This function gets the specific bank the user uses by using their country code and institution name
    def get_institution(self):
        response = requests.get(f"https://ob.nordigen.com/api/v2/institutions/?country={self.Country_code}",
                                headers=self.AUTH
                                ).json()
        # This checks in the bank the user typed in actually exists, we may want to make an interactive method to enter
        # their bank and area code later in the web application
        bankexists = False
        for bank in response:
            if bank['name'] == self.Bank:
                return bank['id']
        if not bankexists:
            print("Incorrect institution name, see the documentation!")

    # This function increases the total historical transaction data we can pull from user history to 365 days from the
    # default 180
    def user_agreement(self):
        data = {"max_historical_days": "365"}
        response = requests.post(f"https://ob.nordigen.com/api/v2/agreements/enduser/",
                                headers=self.AUTH, data=data
                                ).json()
        return response['id']

    # This function provides the user with a link to add their transaction data to our database
    def get_link(self):
        # Note: Change redirect to web application home URL, when developed

        # This while loop checks if a reference id is in use, if it is it will increment the id until it doesnt exist
        # in our "User_ids.txt" file AND has not been used as a reference before
        id_created = False
        id_ = 0
        while not id_created:
            try:
                user_id = unique_id(id_)
                data = {"redirect": "https://www.youtube.com/", "institution_id": f"{self.INSTITUTION_ID}",
                        "reference": f"{user_id}", "agreement": f"{self.AGREEMENT_ID}", "user_language": "EN"}
                response = requests.post("https://ob.nordigen.com/api/v2/requisitions/",
                                         headers=self.AUTH, data=data
                                         ).json()
                add_entry(user_id, response['id'])
                requisition_id = response['id']
                id_created = True
            except KeyError:
                id_ += 1
        print(f'User Id: {user_id} created, with Requisition Id: {requisition_id}')
        # This opens a tab in the default web browser, using the link provided by Nordigen so the user can provide their
        # details, so we can access their transaction data
        webbrowser.open(response['link'])


def main():
    AddUser("gb", "National Westminster Bank")


if __name__ == '__main__':
    main()

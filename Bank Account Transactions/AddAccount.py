import requests
import webbrowser
from GenerateUserID import Unique_id, Add_Entry

class AddUser:
    def __init__(self, country_code, bank):
        self.Country_code = country_code
        self.Bank = bank

        self.ACCESS_TOKEN, self.REFRESH_TOKEN = self.get_accounttoken()

        with open("AccessToken.txt", 'w') as file:
            file.write(f'{self.ACCESS_TOKEN}')

        self.AUTH = {'Authorization': f'Bearer {self.ACCESS_TOKEN}'}

        self.INSTITUTION_ID = self.get_institution()

    def get_accounttoken(self):
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

        User_id = Unique_id()
        Data = {"redirect": "https://www.youtube.com/", "institution_id":f"{self.INSTITUTION_ID}", "reference": f"{User_id}", "user_language": "EN"}
        response = requests.post("https://ob.nordigen.com/api/v2/requisitions/", headers=self.AUTH, data=Data).json()
        Add_Entry(User_id, response['id'])
        webbrowser.open(response['link'])




def main():
    Person = AddUser("gb", "National Westminster Bank")


if __name__ == '__main__':
    main()






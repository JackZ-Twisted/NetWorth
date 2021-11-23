import requests
from AddAccount import AddUser


def get_accounts(self):
    response = requests.get(f"https://ob.nordigen.com/api/v2/requisitions/{self.REQUISITION_ID}/",
                            headers=self.AUTH).json()
    ACCOUNT_IDS = response['accounts']
    with open("Account_Ids.txt", "w") as file:
        file.write(f"\n{ACCOUNT_IDS}")
    return response['accounts']


def get_data(self, ACCOUNT_ID):
    response = requests.get(f"https://ob.nordigen.com/api/v2/accounts/{ACCOUNT_ID}/transactions/",
                            headers=self.AUTH).json()
    print(response)




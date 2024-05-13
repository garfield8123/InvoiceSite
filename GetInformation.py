from apicalls import *
from AdvancedFernetDataEncryption import *
import json

class SyncNumberQuickBooksDelete:
    def __init__(self, start=0, step=1):
        self.current_value = start
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        value = self.current_value
        self.current_value += self.step
        return value

def quickbooksInit():
    synctoken = SyncNumberQuickBooksDelete()
    data, serverData = readConfig()
    production = False
    if (data.get("Environment") != "sandbox"):
        production = True
    companyID = data.get("Company_ID")
    accessToken = data.get("Access_Token")
    return companyID, accessToken, production, synctoken

def readConfig():
    with open("QuickbooksConfig.json") as secretinformation:
        quickbooksData = json.load(secretinformation)
    with open("Server.json") as serverInformation:
        serverData = json.load(serverInformation)
    return quickbooksData, serverData

def Checklogin(password):
    with open('LoginCredentials.txt', 'r') as f:
        text = f.read()
    if dataDecryption(text) == dataDecryption(password):
        return True
    return False

def getWorkOrder(standard):
    if standard:
        return {"PhoneNumber":'''
            <label>Phone Number: </label>
                    <input type="tel" name="CustomerPhoneNumber" placeholder="831-123-1122">''',
                "CustomerInfo":'''<label>Customer Phone Number: </label>
                    <input type="tel" name="CustomerPhoneNumber" placeholder="831-123-1122"> <br>''', 
                    "InvoiceTitle":'''<h3>Standard Invoice</h3>''',
                    "ServicePassword":'''<label>System Administrator Password: </label>
                    <input type="password" name="SystemPassword" placeholder="admin password" required><br>'''}
    return {"PhoneNumber":'''
            <label>Service Phone Number: </label>
                    <input type="tel" name="CustomerPhoneNumber" placeholder="831-123-1122"> 
            <label>Alternative Phone Number: </label>
                    <input type="tel" name="AltPhoneNumber" placeholder="831-123-1122"> <br>''', 
                    "InvoiceTitle":'''<h3>Mobile Invoice</h3>''',
                    "ServicePassword":'''<label>Unlock Phone Password: </label>
                    <input type="password" name="SystemPassword" placeholder="admin password" required><br>'''}
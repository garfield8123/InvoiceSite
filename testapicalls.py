from apicalls import *
import json

def readConfig():
    with open("config.json") as secretinformation:
        data = json.load(secretinformation)
    return data
data = readConfig()
customerRequest = getCustomerInfo(data.get("Company_ID"), data.get("Access_Token"), 1)
print(customerRequest)
print(customerRequest)

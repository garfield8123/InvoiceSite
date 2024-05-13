from GetInformation import *
from apicalls import *


def getCustomerID(fullyQualifiedName= None, primaryEmailAddress= None, primaryPhoneNumber= None):
    companyID, accessToken, production, synctoken = quickbooksInit()
    if primaryEmailAddress is not None:
        query = "select PrimaryEmailAddr from Customer"
        customerInfoJson = APIQueryInfo(companyID, accessToken, query, production)
        for x in customerInfoJson.get("Customer"):
            if x.get("PrimaryEmailAddr") is not None:
                if x.get("PrimaryEmailAddr").get("Address") == primaryEmailAddress:
                    return x.get("Id")
    elif primaryPhoneNumber is not None:
        query = "select PrimaryPhone from Customer"
        customerInfoJson = APIQueryInfo(companyID, accessToken, query, production)
        for x in customerInfoJson.get("Customer"):
            if x.get("PrimaryPhone") is not None:
                if x.get("PrimaryPhone").get("FreeFormNumber") == primaryPhoneNumber:
                    return x.get("Id")
    else:
        query = "select FullyQualifiedName from Customer WHERE FullyQualifiedName='"+fullyQualifiedName+"'"
        customerInfoJson = APIQueryInfo(companyID, accessToken, query, production)
        for x in customerInfoJson.get("Customer"):
            return x.get("Id")

def createCustomer(fullyQualifiedName, primaryEmailAddress="", primaryPhoneNumber="", notes=""):
    companyID, accessToken, production, synctoken = quickbooksInit()
    customerdict = {
        "FullyQualifiedName": fullyQualifiedName, 
        "PrimaryEmailAddr": {
            "Address": primaryEmailAddress
        }, 
        "DisplayName": fullyQualifiedName, 
        "Suffix": "", 
        "Title": "", 
        "MiddleName": "", 
        "Notes": notes, 
        "FamilyName": "", 
        "PrimaryPhone": {
            "FreeFormNumber": primaryPhoneNumber
        }, 
        "GivenName": fullyQualifiedName
        }
    return APICreateCustomerInfo(companyID, accessToken, customerdict, production)

def getCustomerInformation(CustomerID):
    companyID, accessToken, production, synctoken = quickbooksInit()
    customerinfo = APIgetCustomerInfo(companyID, accessToken, CustomerID, production)
    print(customerinfo)

#getCustomerInformation(62)
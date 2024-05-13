from GetInformation import *
from apicalls import *

def createPaymentDict(TotalAmount, customerID):
    companyID, accessToken, production, synctoken = quickbooksInit()
    paymentDict = {
    "TotalAmt": TotalAmount, 
    "CustomerRef": {
        "value": customerID
    }
    }
    return APIcreatePayment(companyID, accessToken, paymentDict, production)

def deletePaymentDict(paymentID, Delete):
    companyID, accessToken, production, synctoken = quickbooksInit()
    deleteDict = {
    "SyncToken": next(synctoken), 
    "Id": paymentID
    }
    if Delete:
        return APIdeletePayment(companyID, accessToken, deleteDict, production)
    return APIvoidPayment(companyID, accessToken, deleteDict, production)

def getPayment(paymentID):
    companyID, accessToken, production, synctoken = quickbooksInit()
    invoiceInfo = APIgetPayment(companyID, accessToken, paymentID, production)
    print(invoiceInfo)

def sendPayment(paymentID, emailAddress):
    companyID, accessToken, production, synctoken = quickbooksInit()
    return APIsendPayment(companyID, accessToken, paymentID, emailAddress, production)
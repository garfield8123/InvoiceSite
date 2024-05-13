from GetInformation import *
from apicalls import *

def addItems(Amount, name, quantity, list):
    inputData = {
        "DetailType": "SalesItemLineDetail", 
        "Amount": Amount, 
        "SalesItemLineDetail": {
            "ItemRef": {
            "name": name, 
            "value": str(quantity)
            }
        }
        }
    list.append(inputData)
    return list

def createInvoice(itemlist, customerID):
    companyID, accessToken, production, synctoken = quickbooksInit()
    invoiceDict=    {
  "Line": itemlist,  
  "CustomerRef": {
    "value": customerID
  }
}  
    return createInvoice(companyID, accessToken, invoiceDict, production)

def deleteVoidInvoice(invoiceID, Delete):
    companyID, accessToken, production, synctoken = quickbooksInit()
    deleteDict = {
    "SyncToken": next(synctoken), 
    "Id": invoiceID
    }
    if Delete:
        return APIdeleteInvoice(companyID, accessToken, deleteDict, production)
    return APIvoidInvoice(companyID, accessToken, deleteDict, production)

def getInvoice(InvoiceID):
    companyID, accessToken, production, synctoken = quickbooksInit()
    invoiceInfo = APIgetInvoice(companyID, accessToken, InvoiceID, production)
    print(invoiceInfo)

def sendInvoice(InvoiceID, emailAddress):
    companyID, accessToken, production, synctoken = quickbooksInit()
    return APIsendInvoice(companyID, accessToken, InvoiceID, emailAddress, production)

'''listofitems = []
addItems(100, "Repair", 1, listofitems)
print(listofitems)
print(createInvoice(listofitems, 62))
print(deleteVoidInvoice(152, False))'''
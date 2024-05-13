from GetInformation import *
from apicalls import *



def createSaleReceipt():
    salesReceiptDict = {
  "Line": [
    {
      "Description": "Pest Control Services", 
      "DetailType": "SalesItemLineDetail", 
      "SalesItemLineDetail": {
        "TaxCodeRef": {
          "value": "NON"
        }, 
        "Qty": 1, 
        "UnitPrice": 35, 
        "ItemRef": {
          "name": "Pest Control", 
          "value": "10"
        }
      }, 
      "LineNum": 1, 
      "Amount": 35.0, 
      "Id": "1"
    }
  ]
}
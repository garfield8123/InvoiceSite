'''
Author: Weibo Yang
Usage: API-Callable methods for Computer Zone 
References: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account
'''
import requests

def error_status(r):
    if r.status_code != 200:
        print("---- Error in attempting Request ----")
        print("Status Code: ", r.status_code)
        print(r.json())

def getbaseURL(production):
    baseUrl = "https://sandbox-quickbooks.api.intuit.com"
    if production:
        baseUrl = "https://quickbooks.api.intuit.com"
    return baseUrl

#---- Handle Customer Information for Quickbooks API ----
#---- Refrence: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customer

def APICreateCustomerInfo(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/customer?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIQueryInfo(companyID, accessToken, queryStatement, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/query?query="+str(queryStatement)+"&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json().get("QueryResponse")

def APIgetCustomerInfo(companyID, accessToken, CustomerID, production=False, minorVersion=65):
    #---- Customer ID Location Reference: https://quickbooks.intuit.com/learn-support/en-us/help-article/customer-company-settings/find-quickbooks-online-company-id/L7lp8O9yU_US_en_US ----
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/customer/"+str(CustomerID)+"?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json()

#---- Handle Invoicing for quickbooks API ----
#---- Refrence: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/invoice

def APIcreateInvoice(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/invoice?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIdeleteInvoice(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/invoice?operation=delete&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIvoidInvoice(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/invoice?operation=void&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIgetInvoicePDF(companyID, accessToken, invoiceID, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/invoice/"+str(invoiceID)+"/pdf?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/octet-stream"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json()

def APIgetInvoice(companyID, accessToken, invoiceID, production=False, minorVersion=65):
    #---- Invoice ID Reference Location: https://help.developer.intuit.com/s/question/0D50f00004tcfgYCAQ/is-there-any-way-to-fetch-the-invoice-id ----
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/invoice/"+str(invoiceID)+"?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json()

def APIsendInvoice(companyID, accessToken, invoiceID, emailAddress, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/invoice/"+str(invoiceID)+"/send?sendTo="+emailAddress+"&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/octet-stream"}
    r = requests.post(url=url, headers=headers)
    error_status(r)
    return r.json()

#---- Handle Payments for Quickbooks API ----
#---- Refrence: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/payment

def APIcreatePayment(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/payment?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIdeletePayment(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/payment?operation=delete&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIvoidPayment(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/payment?operation=update&include=void&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIgetPaymentPDF(companyID, accessToken, paymentID, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/payment/"+str(paymentID)+"/pdf?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/octet-stream"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json()

def APIgetPayment(companyID, accessToken, paymentID, production=False, minorVersion=65):
    #---- Invoice ID Reference Location: https://help.developer.intuit.com/s/question/0D50f00004tcfgYCAQ/is-there-any-way-to-fetch-the-invoice-id ----
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/payment/"+str(paymentID)+"?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json()

def APIsendPayment(companyID, accessToken, paymentID, emailAddress, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/payment/"+str(paymentID)+"/send?sendTo="+emailAddress+"&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/octet-stream"}
    r = requests.post(url=url, headers=headers)
    error_status(r)
    return r.json()

#---- Handle SalesReceipt for Quickbooks API ----
#---- Refrence: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/salesreceipt

def APIcreateSaleReceipt(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/salereceipt?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIdeleteSaleReceipt(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/salesreceipt?operation=delete&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIvoidSaleReceipt(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/salesreceipt?operation=update&include=void&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIgetSaleReceiptPDF(companyID, accessToken, salesReceiptID, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/salesreceipt/"+str(salesReceiptID)+"/pdf?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json()

def APIgetSaleReceipt(companyID, accessToken, salesReceiptID, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/salesreceipt/"+str(salesReceiptID)+"?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json()

def APIsendSaleReceipt(companyID, accessToken, salesReceiptID, emailAddress, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/salesreceipt/"+str(salesReceiptID)+"/send?sendTo="+emailAddress+"&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/octet-stream"}
    r = requests.post(url=url, headers=headers)
    error_status(r)
    return r.json()


#----- Methods that might not exist for all quickbook accounts ----

#---- Handle Purchasing for Quickbooks API ----

def APIcreatePurchase(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/purchase?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIdeletePurcahse(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/purchase?operation=delete&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIgetPurchase(companyID, accessToken, purchaseID, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/purchase/"+str(purchaseID)+"?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json()

#---- Handle bills for Quickbooks API ----

def APIcreateBill(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/bill?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIdeleteBill(companyID, accessToken, payloadJSON, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/bill?operation=delete&minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.post(url=url, json=payloadJSON, headers=headers)
    error_status(r)
    return r.json()

def APIgetBill(companyID, accessToken, billID, production=False, minorVersion=65):
    baseUrl = getbaseURL(production) 
    url = baseUrl+"/v3/company/"+str(companyID)+"/bill/"+str(billID)+"?minorversion="+str(minorVersion)
    headers = {"accept":"application/json", "authorization":"Bearer " + accessToken, "content-type":"application/json"}
    r = requests.get(url=url, headers=headers)
    error_status(r)
    return r.json()
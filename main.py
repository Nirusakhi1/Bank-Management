from create import insert
from read import read
from update import update
from delete import delete

obj=insert()
objread = read()
objupdate=update()
objdelete=delete()

print("----------Bank Management System----------")
print("For Inserting the data press 1 : ")
print("For Reading the data press 2 : ")
print("For Updating the data press 3 : ")
print("For Deleting the data press 4 : ")

opr = int(input("Please enter your operations: "))

def myopr():
    print("-----For Personal information press 1-----")
    print("-----For Bank details press 2-----")
    print("-----For Transaction details press 3-----")
    print("-----For Account details press 4-----")
    vr=int(input("Please select your table : "))
    if vr == 1:
        return "personal_details"
    elif vr == 2:
        return "bank_details"
    elif vr == 3:
        return "transaction_details"
    elif vr == 4:
        return "account_details"

if opr==1:
    h = myopr()
    if h=='personal_details':
        cid = int(input("please enter customer id:"))
        fname = input("please enter customer first name:")
        lname = input("please enter customer last name:")
        addr = input("please eneter customer address:")
        phn = int(input("please enter customer phone number:"))
        adhar = input("please enter customer aadhar number:")
        pan = input("please enter customer pan number:")
        obj.personal_details(cid,fname,lname,addr,phn,adhar,pan)

    elif h=='bank_details':
        acn = int(input("Please enter account number:"))
        cid = int(input("Please enter customerid:"))
        ifsc = input("Please enter ifsc code:")
        actype = input("Please enter account type:")
        obj.bank_details(acn,cid,ifsc,actype)

    elif h=='transaction_details':
        trsnid = input("Please enter your transaction id:")
        sacc = input("Please enter sender account:")
        racc = input("Please enter receiver account:")
        amt = int(input("Please enter amount:"))
        method = input("Please enter payment method:")
        obj.transaction_details(trsnid,sacc,racc,amt,method)

    elif h=='account_details':
        acn = int(input("Please enter account number:"))
        trsnid = input("Please enter transaction id:")
        amt = int(input("Please enter amount:"))
        clsngbal = int(input("Please enter closing balance: "))
        trsntype = input("please enter transaction type: ")
        obj.account_details(acn,trsnid,amt,clsngbal,trsntype)

if opr==2:
    j = myopr()
    cusid = int(input("Please enter customer id for fetching data: "))
    objread.specific_info(cusid,j)
if opr==3:
    j =  myopr()
    cusid = int(input("Please enter customer id for fetching data: "))
    colname = input("Please enter column name: ")
    newval = input("Please enter new values: ")
    objupdate.myupdate(j,colname,newval,cusid)  
if opr==4:
    n = myopr()
    cusid = int(input("Please enter customer id to delete data: "))
    objdelete.mydelete(n,cusid)
        
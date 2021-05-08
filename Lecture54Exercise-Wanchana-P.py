"""
###Function###
"""
def Login():
    UserNameInput = input("UserName : ")
    PasswordInput = input("PassWord : ")
    if UserNameInput == "a" and PasswordInput == "1":
        return True
    else:
        print("Wrong Username Or Password")
        return Login()
def ShowMenu():
    print("-------Welcome---------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def MenuSelect():
    UserSelected = int(input(">>"))
    return UserSelected
def VatCalculate(totalPrice):
    vat = 7
    result = totalPrice +(totalPrice*vat/100)
    return result
def Pricecalculate():
    price1 =int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return VatCalculate(price1+price2)
"""
###Run###
"""
if Login():
    ShowMenu()
    UserSelected = MenuSelect()
    if  UserSelected == 1:
        totalPrice = int(input("Enter totalPrice : "))
        print(VatCalculate(totalPrice))
    elif UserSelected == 2:
            print(Pricecalculate())



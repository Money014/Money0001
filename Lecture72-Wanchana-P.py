menuList = []

def showBill():
    print("----MyFood----")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])



while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.capitalize() == "Exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName,menuPrice])

showBill()

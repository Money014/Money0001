menuList = []
PriceList = []

def showBill():
    total = 0
    print("----MyFood----")
    for i in range(len(menuList)):
        print(menuList[i],PriceList[i])
        total = total + PriceList[i]
    print("Total :",total)


while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.capitalize() == "Exit"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        PriceList.append(menuPrice)

showBill()


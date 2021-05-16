SystemMenu = {"ไก่":40,"ปลา":30,"หมู":50,"หมึก":50}
menuList = []

def showBill():
    print("----MyFood----")
    total =0
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        total = total + menuList[i][1]
    else:
        print(total)



while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.capitalize() == "Exit"):
        break
    else:
        menuList.append([menuName,SystemMenu[menuName]])
print(menuList)
showBill()

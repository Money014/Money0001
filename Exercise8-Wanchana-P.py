UserName = input("Enter UserName : ")
PrassWord = input("Enter PrassWord : ")
Banana   = 10
Fish     = 15
Gold     = 30
Siver    = 20
Water    = 10
Butter   = 20
if UserName == "Babe" and PrassWord == "1234" :
    print("-----------------------")
    print("-------Welcome---------")
    print("1.Banana   10 USD")
    print("2.Fish     15 USD")
    print("3.Gold     30 USD")
    print("4.Siver    20 USD")
    print("5.Water    10 USD")
    print("6.Butter   20 USD")
    P = int(input("Pick Number : "))
    if  P == 1 :
        print("Banana x 1 = ", Banana,"USD")
        x1 = int(input("How many do you want : "))
        print("Price : ",x1*Banana,"USD")
    elif P == 2:
        print("Fish x 1 = ", Fish,"USD")
        x2 = int(input("How many do you want : "))
        print("Pirce : ",x2*Fish,"USD")
    elif P == 3:
        print("Gold x 1 = ", Gold,"USD")
        x3 = int(input("How many do you want : "))
        print("Pirce : ", x3 * Gold,"USD")
    elif P == 4:
        print("Siver x 1 = ", Siver,"USD")
        x4 = int(input("How many do you want : "))
        print("Pirce : ",x4*Siver,"USD")
    elif P == 5:
        print("Water x 1 = ", Water,"USD")
        x5 = int(input("How many do you want : "))
        print("Pirce : ",x5*Water,"USD")
    elif P == 6:
        print("Butter x 1 = ", Butter,"USD")
        x6 = int(input("How many do you want : "))
        print("Pirce : ",x6*Butter,"USD")
else:
    print("Wrong UserName Or PrassWord")







print("--------------------------------")
UserNameInput = input("UserName : ")
PasswordInput = input("PassWord : ")
while UserNameInput != "admin" or PasswordInput != "1234":
    print("--------------------------------")
    UserNameInput = input("UserName : ")
    PasswordInput = input("PassWord : ")
    if UserNameInput != "admin" or PasswordInput != "1234":
        print("That's Wrong")
print("Done")
print("--------------------------------")

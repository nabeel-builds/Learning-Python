import json
import random
import string
from pathlib import Path

class Bank:
    database = "data.json" #Main Data
    data = [] # Dummy Data

    try:

        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No Such file exists")

    except Exception as err:
        print(f"An Error occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,"w") as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountNumberGenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    def CreateAccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email": input("Tell your email: "),
            "pin": int(input("Tell your 4 digits pin: ")),
            "accountNo.": Bank.__accountNumberGenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you can not create your account")
        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()


    def DepositMoney(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]

        if userdata == False:
            print("Sorry No data found")
        else:
            amount = int(input("How much you want to deposit: "))
            if amount > 10000 or amount < 0:
                print("Sorry the amount is too much you can deposit below 10000 and above 0")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount Deposited successfully")


    def WithdrawlMoney(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]

        if userdata == False:
            print("Sorry No data found")
        else:
            amount = int(input("How much you want to withdrwal: "))
            if userdata[0]['balance'] < amount:
                print("Sorry you don't have that much money")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount Withfrew successfully")


    def ShowDetails(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]
        print("\n\n Your information are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def UpdateDetails(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]

        if userdata == False:
            print("No Such User Found")
        else:
            print("You cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("Please tell your new NAME or press enter to skip: "),
                "email": input("Please tell your new EMAIL or press enter to skip: "),
                "pin": input("Please tell your new PIN or press enter to skip: "),
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] = userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]

            newdata["age"] = userdata[0]["age"]
            newdata["accountNo."] = userdata[0]["accountNo."]
            newdata["balance"] = userdata[0]["balance"]

            if type(newdata["pin"]) == str:
                newdata["pin"] = int(newdata["pin"])


            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details updated successfully")
                

    def DeleteAccount(self):

        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]

        if userdata == False:
            print("No such Data exists")
        else:
            check = input("Press Y if you actually want to delete the account or press N: ")
            if check == "n" or check == "N":
                print("Bypassesed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully")
                Bank.__update()

user = Bank()

print("Press 1 for creating an account")
print("Press 2 for Deposit Money in the Bank")
print("Press 3 for Withdrawl Money in the Bank")
print("Press 4 for Details")
print("Press 5 for Updating the Details")
print("Press 6 for Deleting your Bank account")


check = int(input("Tell your response: "))

if check == 1:
    user.CreateAccount()

if check == 2:
    user.DepositMoney()

if check == 3:
    user.WithdrawlMoney()

if check == 4:
    user.ShowDetails()

if check == 5:
    user.UpdateDetails()

if check == 6:
    user.DeleteAccount()
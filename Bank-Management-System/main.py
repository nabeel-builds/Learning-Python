import json
import random
import string
from pathlib import Path

class Bank:
    database = "data.json"
    data = []

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

        for i in Bank.data


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
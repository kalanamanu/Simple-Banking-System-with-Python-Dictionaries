details = {"kalana": {
    "pw": "kalana123",
    "balance": 5000,
    "activity_Status": True
    },
    "bashitha": {
        "pw": "bashitha123",
        "balance": 5000,
        "activity_Status": True
    },

    "mahesh": {
        "pw": "mahesh123",
        "balance": 5000,
        "activity_Status": True
    }
}



def create_a_account():
    user_name = input("Enter an user name: ")
    pass_word = input("Enter password: ")
    deposited_balance = int(input("Enter amount to deposit: "))

    if user_name not in details.keys():
        details[user_name] = {}

        details[user_name]["pw"] = pass_word
        details[user_name]["balance"] = deposited_balance
        details[user_name]["activity_Status"] = True
        print("You Registered!! Now you can login to our system.")
        login(user_name, pass_word)
    else:
        print("User name all ready taken, Enter a new user name.")
        create_a_account()


def login(user_name, pass_word):
    if user_name in details and pass_word == details[user_name]["pw"]:
        print("Login Successful!")
        action()
    else:
        print("Invalid user name or password!")


def transactions_between_acc():
    get_input_1 = int(input("Enter a amount: "))
    if get_input_1 < details[user_name]["balance"]:
        get_input_2 = input("Enter acc name: ")
        details[get_input_2]["balance"] += get_input_1
        details[user_name]["balance"] -= get_input_1
        print("Now your account balance is :", details[user_name]["balance"])
        action()
    else:
        print("Sorry your account balance is insufficient.")
        transactions_between_acc()

def action():
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Transactions")
    print("5. Exit")

    choice = input("Enter your action: ")

    if choice == "1":
        new_deposit = int(input("Enter the amount to deposit: "))
        details[user_name]["balance"] += new_deposit
        new_balance = details[user_name]["balance"]
        print("Now your balance is: ",new_balance)
        action()
    elif choice == "2":
        withdraw_money = int(input("How much need you to withdraw: "))
        if withdraw_money < details[user_name]["balance"]:
            details[user_name]["balance"] -= withdraw_money
            new_balance_after_withdraw = details[user_name]["balance"]
            print("Now your balance is: ",new_balance_after_withdraw)
            action()
        elif print("Insufficient account balance. Try again!"):
            action()
    elif choice == "3":
        print("Your current account balance is: ", details[user_name]["balance"])
        action()
    elif choice == "4":
        transactions_between_acc()
    elif choice == "5":
        print("Thankyou for E-banking!!")
        exit()
    else:
        print("Invalid action!")
        action()



while True:
    print("Welcome to KMJ Bank")
    get_login_or_register = input("If you have a account Login not Register: ")
    if get_login_or_register == "login":
        print("login")
        user_name = input("Enter an user name: ")
        pass_word = input("Enter password: ")
        login(user_name, pass_word)
    elif get_login_or_register == "register":
        print("Register")
        create_a_account()
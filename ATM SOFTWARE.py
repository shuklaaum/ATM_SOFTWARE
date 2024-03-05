#class name is always in Pasacal case
class Atm:
    #constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi! How may I help you ?
        1. Press 1 to create pin.
        2. Press 2 to change pin.
        3. Press 3 to check  balance.
        4. Press 4 to withdraw.
        5. Anything else to exit.        
        """)

        if user_input == "1":
            #create pin
            self.create_pin()
        elif user_input == "2":
            #change pin
            self.change_pin()
        elif user_input == "3":
            #check_balance
            self.check_balance()
        elif user_input == "4":
            # withdraw
            self.withdraw()
        else:
            exit()

        self.menu()

    def create_pin(self):
        user_pin = input("Enter your pin")
        self.pin = user_pin

        user_balance = int(input('Enter Balance'))
        self.balance = user_balance

        print("Pin created successfully")

    def change_pin(self):
        old_pin = input("Enter old pin")
        if old_pin == self.pin:
            #Let him change pin
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print("Pin changed successfully")

        else:
            print("Nahi kar sakta re baba")


    def check_balance(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            print("Your Balance is ", self.balance)
        else:
            print("chal nikal yahan se")

    def withdraw(self):
        user_input = input("Enter your pin")
        if user_input == self.pin:
            # allow to withdraw
            amount = int(input("What's the amount you want?"))
            if amount > self.balance:
                print("Exceeding balance amount")
                print("Your balance is ", self.balance)

            else:
                print("Withdrawal successful")
                print("Your left balance is ", self.balance - amount)


        else:
            print("your password is incorrect")





obj = Atm()

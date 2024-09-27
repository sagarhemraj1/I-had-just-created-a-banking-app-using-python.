# Simple Online Banking System

class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. Your new balance is: ${self.balance:.2f}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. Your new balance is: ${self.balance:.2f}.")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}.")

# Creating user accounts (this will store in-memory for now)
users = {}

# Function for creating new accounts
def create_account():
    username = input("Create a username: ")
    if username in users:
        print("Username already exists. Please try a different username.")
        return
    password = input("Create a password: ")
    users[username] = BankAccount(username, password)
    print(f"Account created successfully for {username}!")

# Function for logging into an existing account
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username].password == password:
        print(f"Welcome, {username}!")
        return users[username]
    else:
        print("Invalid username or password. Please try again.")
        return None

def banking_menu(account):
    while True:
        print("\nBanking Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Log Out")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\nWelcome to the Online Banking System!")
        print("1. Create New Account")
        print("2. Log In")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            account = login()
            if account:
                banking_menu(account)
        elif choice == "3":
            print("Thank you for using the online banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# CSC 2080 - Homework Assignment #11

import json

# Exercise 3: Conference Attendee Tracker
class Conference:
    def __init__(self, filename="attendees.json"):
        self.filename = filename
        try:
            # Load existing attendees from file
            with open(self.filename, "r") as file:
                self.attendees = json.load(file)
        except FileNotFoundError:
            # Initialize an empty list if file doesn't exist
            self.attendees = []

    def save_attendees(self):
        # Save the attendees list to a file
        with open(self.filename, "w") as file:
            json.dump(self.attendees, file)

    def add_attendee(self, name, company, state, email):
        # Add a new attendee to the list
        self.attendees.append({"name": name, "company": company, "state": state, "email": email})
        self.save_attendees()

    def display_attendee(self, name):
        # Display information of a specific attendee
        for attendee in self.attendees:
            if attendee["name"] == name:
                return attendee
        return None

    def delete_attendee(self, name):
        # Remove an attendee by name
        self.attendees = [a for a in self.attendees if a["name"] != name]
        self.save_attendees()

    def list_all_attendees(self):
        # List names and emails of all attendees
        return [(a["name"], a["email"]) for a in self.attendees]

    def list_attendees_by_state(self, state):
        # List names and emails of attendees from a specific state
        return [(a["name"], a["email"]) for a in self.attendees if a["state"] == state]

# Example usage for Exercise 3
def conference_example():
    conf = Conference()
    conf.add_attendee("Alice", "TechCorp", "CA", "alice@techcorp.com")
    conf.add_attendee("Bob", "HealthInc", "NY", "bob@healthinc.com")
    print("All attendees:", conf.list_all_attendees())
    print("Attendees from NY:", conf.list_attendees_by_state("NY"))
    print("Details for Alice:", conf.display_attendee("Alice"))
    conf.delete_attendee("Alice")
    print("After deletion:", conf.list_all_attendees())

# Exercise 4: ATM Simulation
class ATM:
    def __init__(self, filename="accounts.json"):
        self.filename = filename
        try:
            # Load account data from file
            with open(self.filename, "r") as file:
                self.accounts = json.load(file)
        except FileNotFoundError:
            # Initialize empty accounts if file doesn't exist
            self.accounts = {}

    def save_accounts(self):
        # Save account data to a file
        with open(self.filename, "w") as file:
            json.dump(self.accounts, file)

    def add_account(self, user_id, pin, checking=0, savings=0):
        # Add a new account with initial balances
        self.accounts[user_id] = {"pin": pin, "checking": checking, "savings": savings}
        self.save_accounts()

    def authenticate(self, user_id, pin):
        # Verify user ID and PIN
        account = self.accounts.get(user_id)
        return account and account["pin"] == pin

    def get_balance(self, user_id, account_type):
        # Get the balance of a specified account type
        return self.accounts[user_id][account_type]

    def withdraw(self, user_id, account_type, amount):
        # Withdraw amount from specified account type
        if self.accounts[user_id][account_type] >= amount:
            self.accounts[user_id][account_type] -= amount
            self.save_accounts()
            return True
        return False

    def transfer(self, user_id, from_account, to_account, amount):
        # Transfer amount between accounts
        if self.accounts[user_id][from_account] >= amount:
            self.accounts[user_id][from_account] -= amount
            self.accounts[user_id][to_account] += amount
            self.save_accounts()
            return True
        return False

# Example usage for Exercise 4
def atm_example():
    atm = ATM()
    atm.add_account("user1", "1234", checking=500, savings=1000)
    user_id = "user1"
    pin = "1234"

    if atm.authenticate(user_id, pin):
        print("Authenticated!")
        print("Checking balance:", atm.get_balance(user_id, "checking"))
        print("Savings balance:", atm.get_balance(user_id, "savings"))
        if atm.withdraw(user_id, "checking", 200):
            print("Withdraw successful. New checking balance:", atm.get_balance(user_id, "checking"))
        if atm.transfer(user_id, "savings", "checking", 300):
            print("Transfer successful. New balances:")
            print("Checking:", atm.get_balance(user_id, "checking"))
            print("Savings:", atm.get_balance(user_id, "savings"))

# Main function to test both exercises
if __name__ == "__main__":
    print("--- Conference Example ---")
    conference_example()
    print("--- ATM Example ---")
    atm_example()

"""
Author: Noa Kirschbaum
Assignment / Part: HW5 - Q1
Date due: 2022-06-28
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

"""
Input file: unknown number of lines of input. 
Each line is a command with info about the command.
File will end with an empty line! (\n)

Each account number is unique, but names can be repeated.
"""


class Account:

    def __init__(self, acc_name, acc_number):
        self.name = acc_name
        self.acc_number = acc_number
        self.balance = 0.00
        # only include accepted transactions in list
        self.transactions = []

    def __str__(self):
        return str(self.acc_number)

    def get_account_num(self):
        return self.acc_number

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def set_balance(self, new_balance):
        self.balance = new_balance

    def get_transactions(self):
        return self.transactions

    def set_transaction(self, added_transaction):
        self.transactions.append(added_transaction)


def print_account_data(acc_list, entered_acc_num):
    existing_account = False
    for account_item in acc_list:
        if account_item.get_account_num() == entered_acc_num:
            current_account = account_item
            existing_account = True
            break
    if existing_account:
        all_transactions = current_account.get_transactions()
        change_list = []
        for transaction_item in all_transactions:
            if transaction_item[0] == 'Deposit':
                change_list.append('+' + str(transaction_item[2] - transaction_item[1]))
            elif transaction_item[0] == 'Withdraw':
                change_list.append('-' + str(transaction_item[1] - transaction_item[2]))

        print("Account: {} ({}), ${}".format(current_account.get_name(), current_account.get_account_num(),
                                             current_account.get_balance()), end=" [")
        for change_ind in range(len(change_list)):
            if change_ind < len(change_list) - 1:
                print(change_list[change_ind], end=", ")
            else:
                print(change_list[change_ind], end="")
        print(']', end='\n')


def deposit_amount(acc_list, entered_acc_num, in_amount):
    """IF the entered num matches an existing acc number,
        then amount is added to balance"""

    existing_account = False
    for account_item in acc_list:
        if account_item.get_account_num() == entered_acc_num:
            current_account = account_item
            existing_account = True
            break
    if not existing_account:
        raise IndexError("This number {} does not match any existing account.".format(entered_acc_num))

    original_balance = current_account.get_balance()

    try:
        current_balance = original_balance + float(in_amount)
    except ValueError as val_error:
        print(val_error, "Amount to deposit is not a Float.")
        raise

    current_account.set_balance(current_balance)

    add_transaction(current_account, ('Deposit', original_balance, current_balance))


def withdraw_amount(acc_list, entered_acc_num, out_amount):
    """If the entered num matches an existing acc number,
        then amount is subtracted ONLY if acc balance > withdraw amount"""

    existing_account = False
    for account_item in acc_list:
        if account_item.get_account_num() == entered_acc_num:
            existing_account = True
            current_account = account_item
            break
    if not existing_account:
        raise IndexError("This number {} does not match any existing account.".format(entered_acc_num))

    original_balance = current_account.get_balance()

    try:
        current_balance = original_balance - float(out_amount)
    except ValueError as val_error:
        print(val_error, "Amount to deposit is not a Float.")
        raise

    if current_balance > 0:
        current_account.set_balance(current_balance)
        add_transaction(current_account, ('Withdraw', original_balance, current_balance))


def add_transaction(current_account, new_transaction):
    """ adds transaction to list. (name, amount changed, balance)"""
    current_account.set_transaction(new_transaction)


def run_command(acc_list, in_command):
    """ return the new acc_list """
    if in_command[0] == "Account":
        try:
            new_account = Account(in_command[1], in_command[2])
        except IndexError as ind_err:
            print(ind_err, "Missing information.")
            raise
        else:
            try:
                int(in_command[2])
            except ValueError:
                print("Value Error: Account Number must be an Integer.")
                raise
            else:
                if in_command[2] not in acc_list:
                    acc_list.append(new_account)
                else:
                    raise Exception("Account already created!")

    elif in_command[0] == "Deposit":
        if len(in_command) < 3:
            raise IndexError("Missing Deposit Information.")
        else:
            deposit_amount(acc_list, in_command[1], in_command[2])

    elif in_command[0] == "Withdraw":
        if len(in_command) < 3:
            raise IndexError("Missing Withdraw Information.")
        else:
            withdraw_amount(acc_list, in_command[1], in_command[2])

    elif in_command[0] == "Print":
        if len(in_command) < 2:
            raise IndexError("Missing Print Information.")
        else:
            print_account_data(acc_list, in_command[1])
    else:
        raise ValueError("Invalid Command.")

    return acc_list


def generate_account_list(file_name):
    while True:
        try:
            file_commands = open(file_name, 'r')
            break
        except FileNotFoundError:
            file_name = input("Enter a new filename: ")
            pass
    accounts_list = []
    for line in file_commands:
        in_command = line.strip().split()

        accounts_list = run_command(accounts_list, in_command)

    file_commands.close()


def main():
    generate_account_list('transactions.txt')


if __name__ == "__main__":
    main()

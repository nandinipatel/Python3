#Author: Nandini Patel
#Date: May 11, 2020
#Description: Methods in Python

import datetime
import pytz

#no name classes, start with capital letters for each new word by convention
#names starting with _ are considered to be non-public; not intended to be modified
class Account:
    """ Simple account class with balance """

    #a static method is shared by all instances of the class; to do so, put @staticmethod above class definition
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        self.show_balance()
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.show_balance()
        else:
            print("The amount must be greater than 0 and less than your account balance")
    
    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        #below, Python upacks the tuple(transction_list) into two variables at a time(date and time)
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
                self._transaction_list.append((Account._current_time(), -amount))
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == "__main__":
    nandini = Account("Nandini", 0)
    nandini.show_balance()

    nandini.deposit(1000)
    nandini.withdraw(500)
    nandini.show_transactions()

    bittu = Account("Bittu", 800)
    bittu.deposit(100)
    bittu.withdraw(200)
    bittu.show_transactions()

    print(bittu.__dict__)
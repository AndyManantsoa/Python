#WAP to implement simple class ad object creation.

class atm:
    def __init__(self, balance=0, pin=1234):
        self.balance = balance
        self.pin = pin
    def display(self):
        print(f"Your balance is : {self.balance}")

SBI=atm(3500,6789)
SBI.display()

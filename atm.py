import os
import shutil

class   atm(object):
    def init (self, gender, age, pin, level, cashwithdrawal, balanceenquiry):

        self.gender = gender
        self.age = age
        self.pin = pin
        self.level = level
        self.cashwithdrawal = cashwithdrawal
        self.balanceenquiry = balanceenquiry

    def gender(self):
        Gender=int(input("Male or Female"))
        print (Gender)

    def age(slef):
        Age=int(input("Your age"))
        print (Age)
    
    def pin(self):
        Pin=int(input("Your pin(6 Digits)"))
        print (Pin)
    
    def cashwithdrawal(self):
        Cashwithdrawal=int(input("Withdraw your cash"))
        print (Cashwithdrawal)

    def balanceenquiry(self):
        Balanceenquiry=int(input("Cash in your account"))
        print (Balanceenquiry)
    
atm()

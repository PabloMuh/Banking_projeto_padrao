from auxiliar import *
from interface import *
from Subject import *
from tkinter import *
import random

from interface import Subject

def clear_window(janela):
        for widget in janela.winfo_children():
            widget.destroy()

class AbortTransaction(Exception):
    '''raise this exception to abort a bank transaction'''
    pass
class account(Observer):
    def __init__(self,code,password):
        self.code = code
        self.password = password
        self.balance = 0
        self.history = []
        self.bill = []
        self.value = []
        self._subjectlist = []
        self.currency = 1
        self.check = False
        self.show = False
    
    def manager_info(self):
        print(f"{self.code} transactions:")
        self.show_transactions()
    def clear_window(janela):
        for widget in janela.winfo_children():
            widget.destroy()

    def add(self,subject):
        self._subjectlist.append(subject)

    def delete(self,subject):
        self._subjectlist.remove(subject)
    def update(self, subject: Subject) -> None:
        return subject.info_investiment()
    def validatevalue(self, value):
        try:
            value = int(value)
        except ValueError:
            raise AbortTransaction('Value must be an integer')
        if value <= 0:
            raise AbortTransaction('Value must be positive')
        return value 
    def get_balance(self):
        return self.balance
    def deposit(self, value):
        value = self.validatevalue(value)
        self.balance += value
        self.balance = round(self.balance, 2)
        self.history.append(f"You made a deposit of {value}. Your account balance after this is {self.balance}")

    def withdraw(self,value):
        value = self.validatevalue(value)
        if self.balance >= value:
            self.balance = self.balance - value
            self.balance = round(self.balance, 2)
            self.history.append(f"You realize a withdraw of {value}. Your accout balance after this is {self.balance}")
        else:
            raise AbortTransaction("You are unable to withdraw this value")

    def transfer(self,account_list,code,original):
            check_transfer = False

            if code == self.code:
                raise AbortTransaction("You can't transfer to your own account")
            for destine in account_list:
                if code == destine.code:
                    check_transfer = True
                    break  

            if check_transfer:
                original = self.validatevalue(original)
                if original <= self.balance:
                    if self.currency == 1 and destine.currency == 2:
                        value = convert_currency(original, 'BRL', 'USD')
                    elif self.currency == 1 and destine.currency == 3:
                        value = convert_currency(original, 'BRL', 'EUR')
                    elif self.currency == 2 and destine.currency == 1: 
                        value = convert_currency(original, 'USD', 'BRL')
                    elif self.currency == 2 and destine.currency == 3:
                        value = convert_currency(original, 'USD', 'EUR')
                    elif self.currency == 3 and destine.currency == 1:
                        value = convert_currency(original, 'EUR', 'BRL')
                    elif self.currency == 3 and destine.currency == 2:
                        value = convert_currency(original, 'EUR', 'USD')
                    else:
                        value = original
                    self.balance -= original
                    self.balance = round(self.balance, 2)
                    destine.balance += value
                    destine.balance = round(destine.balance, 2)
                    self.history.append(f"You transferred {value} to account {destine.code}")
                    destine.history.append(f"You received {value} of the account {self.code}")
                    print(f"Transfer of {round(value,2)} to account {destine.code} completed successfully.")
                else:
                    raise AbortTransaction("You do not have sufficient funds for this transfer.")          
            else:
                raise AbortTransaction("Account not found, you will be redirected to your home page!!!")

    def bills(self,choice):
        check = False
        if self.bill:
            check = True
            choice = choice.lower()

            if choice == "y":
                value = self.value[0]
            else:
                return
        if value > self.balance:
            self.bill.append(f"you have a bill of {value}")
            raise AbortTransaction("You are unable to pay this bill")
        else:
            self.balance -= value
            self.balance = round(self.balance, 2)
            self.history.append(f"You paid the bill with the value {value}")
            if check:
                self.bill.pop(0)
                self.value.pop(0)
    def loan(self,loan_value,check_loan):
        loan_value = self.validatevalue(loan_value)
        loan_value_after = loan_value * 1.07
        loan_value = round(loan_value,2)
        
        if check_loan == "y":
            self.balance += loan_value
            self.balance = round(self.balance, 2)
            self.bill.append(f"You have a bill of {loan_value_after} with the bank")
            self.history.append(f"You took out a loan of {loan_value} from the bank ")
            self.value.append(loan_value_after)
        else:
            raise AbortTransaction("The Loan was reffused, you will be redirected to the central") 
        
    def investiment(self,investiment_choice,investiment_check):

        investiment_choice = self.validatevalue(investiment_choice)

        if investiment_choice == 1:
            if investiment_check == "y":
                self.balance = self.balance * 1.0826
                if check_instance(self._subjectlist,investiment_market):
                    subject = investiment_market()
                    self.add(subject)
                    subject.attach(self,"Investiment")
                else:
                    subject = encontrar_objeto(self._subjectlist,investiment_market)
                subject.addpercentage(8.26)

        elif investiment_choice == 2:
            if investiment_check == "y":
                probability = random.randint(0,100)
                if probability < 98:
                    self.balance = self.balance * 1.1182  
                    percentage = 11.82              
                else:
                    self.balance = self.balance * 0.881
                    percentage = -11.9
                if check_instance(self._subjectlist,investiment_market):
                    subject = investiment_market()
                    self.add(subject)
                    subject.attach(self,"Investiment")
                else:
                    subject = encontrar_objeto(self._subjectlist,investiment_market)
                subject.addpercentage(percentage)

        elif investiment_choice == 3:
            if investiment_check == "y":  
                probability = random.randint(0,200)
                self.balance = self.balance * (probability / 100) 
                if check_instance(self._subjectlist,investiment_market):
                    subject = investiment_market()
                    self.add(subject)
                    subject.attach(self,"Investiment")
                else:
                    subject = encontrar_objeto(self._subjectlist,investiment_market)
                subject.addpercentage(probability - 100)
        elif investiment_choice == 4:
            subject = encontrar_objeto(self._subjectlist,investiment_market)
            if subject == None:
                raise AbortTransaction("You are not part of this group")
            subject.detach(self,"Investiment")
            self.delete(subject)
            return
        else:
            raise AbortTransaction("invalid Choice")
                           
        self.balance = round(self.balance,2)
        
    def convert(self,select):

        select = self.validatevalue(select)

        if select == 2 and self.currency == 1:
            self.balance = convert_currency(self.balance, 'BRL', 'USD') 
            self.currency = 2        
        elif select == 3 and self.currency == 1:
            self.balance = convert_currency(self.balance, 'BRL', 'EUR')  
            self.currency = 3
        elif select == 1 and self.currency == 2:
            self.balance = convert_currency(self.balance, 'USD', 'BRL') 
            self.currency = 1
        elif select == 1 and self.currency == 3:
            self.balance = convert_currency(self.balance, 'EUR', 'BRL')     
            self.currency = 1
        elif select == 2 and self.currency == 3:
            self.balance = convert_currency(self.balance, 'EUR', 'USD') 
            self.currency = 1
        elif select == 3 and self.currency == 2:
            self.balance = convert_currency(self.balance, 'USD', 'EUR') 
            self.currency = 1
        else:
            raise AbortTransaction("You already have this money currency")

        self.history.append("You convert your money")
        self.balance = round(self.balance, 2)
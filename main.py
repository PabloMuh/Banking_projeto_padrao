from auxiliar import *
from operations import *
from bank import *
from tkinter import *

account_list = []

check = True

url = 'https://static.vecteezy.com/system/resources/thumbnails/004/566/136/small/bank-check-cheque-template-free-vector.jpg'
filename = 'cheque.jpg'

def clear_window():
    for widget in janela.winfo_children():
        widget.destroy()
def create():
    clear_window()
    texto = Label(janela,text="Account created successfully")
    texto.grid(column=0,row=0)

    button = Button(janela,text="NEXT",command=show_main_menu)
    button.grid(column=0,row=1)

def choice1(code,password):
    check_object = access_account(code,password)

    if any(check_object.code == obj.code for obj in account_list):
        error = True
        show_login_menu()
        return

    account_list.append(check_object)
    create()
def choice2(code,password):
        for obj in account_list:
            if code == obj.code and password == obj.password:
                show_bank_menu(obj)
                return

        if check:
            print("Account not found, you will be redirected to the home page")

        check = True

def show_register_menu():
    # Limpar a janela e mostrar o menu de login
    clear_window()

    login_label = Label(janela, text="Login Menu")
    login_label.grid(row=0, column=0)

    # Campos de entrada para email e senha
    email_label = Label(janela, text="Code:")
    email_label.grid(row=1, column=0)
    email_entry = Entry(janela)
    email_entry.grid(row=1, column=1)

    senha_label = Label(janela, text="Password:")
    senha_label.grid(row=2, column=0)
    senha_entry = Entry(janela, show="*")  # Para ocultar a senha
    senha_entry.grid(row=2, column=1)

    # Botão de login
    login_button = Button(janela, text="Login", command=lambda: choice1(email_entry.get(), senha_entry.get()))
    login_button.grid(row=4, columnspan=2)
def show_login_menu():
    # Limpar a janela e mostrar o menu de login
    clear_window()
    login_label = Label(janela, text="Menu de Login")
    login_label.grid(row=0, column=0)

    # Campos de entrada para email e senha
    email_label = Label(janela, text="Code:")
    email_label.grid(row=1, column=0)
    email_entry = Entry(janela)
    email_entry.grid(row=1, column=1)

    senha_label = Label(janela, text="Password:")
    senha_label.grid(row=2, column=0)
    senha_entry = Entry(janela, show="*")  # Para ocultar a senha
    senha_entry.grid(row=2, column=1)

    # Botão de login
    login_button = Button(janela, text="Login", command=lambda: choice2(email_entry.get(), senha_entry.get()))
    login_button.grid(row=3, columnspan=2)
def show_main_menu():
    clear_window()
    texto = Label(janela,text='''Welcome to Metropolitan Bank
What do you want to do?''')
    texto.grid(column=0,row=0)

    button1 = Button(janela,text="Register an account",command=show_register_menu)
    button1.grid(column=0,row=1)

    button2 = Button(janela,text="Access your account",command=show_login_menu)
    button2.grid(column=0,row=2)
def show_bank_menu(self):
    clear_window()
    texto = Label(janela,text= "Hello User, Welcome to central administration, What operation do you want to do?")
    texto.grid(column=0,row=0)
    Button1 = Button(janela,text="Deposit",command = lambda:dep(self))
    Button1.grid(column=0,row=1)
    Button2 = Button(janela,text="Withdraw",command = lambda:wit(self))
    Button2.grid(column=0,row=2)
    button3 = Button(janela,text="See my current balance",command=lambda:show_balance(self))
    button3.grid(column=0,row=3)
    button4 = Button(janela,text="Transference",command=lambda:transf(self))
    button4.grid(column=0,row=4)
    button5 = Button(janela,text="Request a check book",command=lambda:cheque(self))
    button5.grid(column=0,row=5)
    button6 = Button(janela,text="Convert currency",command=lambda:convert_currency(self))
    button6.grid(column=0,row=6)
    button7 = Button(janela,text="See the history",command=lambda:history(self))
    button7.grid(column=0,row=7)
    button8 = Button(janela,text="Bills",command=lambda:bill(self))
    button8.grid(column=0,row=8)
    button9 = Button(janela,text="Loan",command=lambda:loan_m(self))
    button9.grid(column=0,row=9)
    button10 = Button(janela,text="Investiment",command=lambda:investiment(self))
    button10.grid(column=0,row=10)
    button11 = Button(janela,text="Quit",command=show_main_menu)
    button11.grid(column=0,row=11)

def show_balance(self):
    clear_window()
    if self.currency == 1:
        currency = "Reais"
    elif self.currency == 2:
        currency = "Dollars"
    else:
        currency = "Euros"
    texto = Label(janela,text= f"Your current balance is {self.get_balance()} {currency}")
    texto.grid(column=0,row=0)

    button = Button(janela,text="Enter",command= lambda: show_bank_menu(self))
    button.grid(column=0,row=1)
def agree_terms(self,choice):
    clear_window()
    texto = Label(janela,text="To make this investment, you will have to agree to make your data and transactions available, for constant updating of your personal and market financial situation.")
    texto.grid(column=0,row=0)

    button_yes = Button(janela,text="Yes",command=lambda:checkPassword(self,7,choice,self))
    button_yes.grid(column=0,row=1)

    button_no = Button(janela,text="No",command=lambda:show_bank_menu(self))
    button_no.grid(column=0,row=2)

def checkpasswordpass(self, password, choice, value,destine):
    if password != self.password:
        clear_window()
        texto = Label(janela,text="The Password is incorrect")
        texto.grid(column=0,row=0)

        button = Button(janela,text="Enter",command= lambda: show_bank_menu(self))
        button.grid(column=0,row=1)   
    else:
        try:
            if choice == 1:
                self.deposit(value)
                show_balance(self)
                return
            elif choice == 2:
                self.withdraw(value)
                show_balance(self)
                return
            elif choice == 3:
                self.transfer(account_list,destine,value)
            elif choice == 4:
                self.convert(value)
                show_balance(self)
                return
            elif choice == 5:
                self.bills("y")
            elif choice == 6:
                self.loan(value,"y")
                show_balance(self)
                return
            elif choice == 7:
                self.investiment(value,"y")
                show_balance(self)
                return
            show_bank_menu(self)
        except AbortTransaction as error:
            clear_window()
            texto = Label(janela,text=str(error))
            texto.grid(column=0,row=0)

            button = Button(janela,text="Enter",command= lambda: show_bank_menu(self))
            button.grid(column=0,row=1)   

def checkPassword(self, choice, value,destine):
    clear_window()
    label = Label(janela, text="Enter your password to confirm the transaction:")
    label.grid(column=0,row=0)

    password = Entry(janela, show="*")
    password.grid(column=0,row=1)

    button = Button(janela,text="Enter",command= lambda:checkpasswordpass(self, password.get(), choice, value,destine))
    button.grid(column= 0,row=2)

def dep(self):
    clear_window()
    texto = Label(janela, text="Enter the value of transaction")
    texto.grid(row=0, column=0)

    value_entry = Entry(janela)
    value_entry.grid(row=1, column=0)

    button = Button(janela, text="Enter", command=lambda: checkPassword(self,1, value_entry.get(),self))
    button.grid(column=0, row=2)

    quit_button = Button(janela,text="Quit",command=lambda:show_bank_menu(self))
    quit_button.grid(column=0,row=3)

def wit(self):
    clear_window()
    texto = Label(janela, text="Enter the value of transaction")
    texto.grid(row=0, column=0)

    value_entry = Entry(janela)
    value_entry.grid(row=1, column=0)

    button = Button(janela, text="Enter", command=lambda: checkPassword(self,2, value_entry.get(),self))
    button.grid(column=0, row=2)

    quit_button = Button(janela,text="Quit",command=lambda:show_bank_menu(self))
    quit_button.grid(column=0,row=3)

def transf(self):
    clear_window()
    texto = Label(janela, text="Enter the value of transaction")
    texto.grid(row=0, column=0)

    value_entry = Entry(janela)
    value_entry.grid(row=0, column=1)

    texto2 = Label(janela,text="Enter the code of the account you want transfer")
    texto2.grid(column=0,row=1)

    destiny_entry = Entry(janela)
    destiny_entry.grid(row=1,column=1)

    button = Button(janela, text="Enter", command=lambda: checkPassword(self,3, value_entry.get(),destiny_entry.get()))
    button.grid(column=0, row=2)

    quit_button = Button(janela,text="Quit",command=lambda:show_bank_menu(self))
    quit_button.grid(column=0,row=3)

def cheque(self):
    clear_window()
    download_file(url,filename)
    texto = Label(janela,text="the check was written off")
    texto.grid(column=0,row=0)

    button = Button(janela,text="Enter",command= lambda: show_bank_menu(self))
    button.grid(column=0,row=1)
def convert_currency(self):
    clear_window()
    texto = Label(janela,text="Choose you new currency")
    texto.grid(column=0,row=0)

    button1 = Button(janela,text="Real",command=lambda:checkPassword(self,4,1,self))
    button1.grid(column=0,row = 1)

    button2 = Button(janela,text="Dollar",command=lambda:checkPassword(self,4,2,self))
    button2.grid(column=0,row = 2)

    button3 = Button(janela,text="Euro",command=lambda:checkPassword(self,4,3,self))
    button3.grid(column=0,row = 3)

    quit_button = Button(janela,text="Quit",command=lambda:show_bank_menu(self))
    quit_button.grid(column=0,row=4)
    
def history(self):
    clear_window()
    texto = Text(janela, height=10, width=40)
    texto.grid(column=0,row=0)

    for item in self.history:
        texto.insert(END, f"{item}\n")
    
    button = Button(janela,text="Enter",command=lambda: show_bank_menu(self))
    button.grid(column=0,row=1)
def bill(self):
    clear_window()
    if self.bill:
        texto = Label(janela,text=f'''{self.bill[0]}
Do you want pay the bill?''')
        texto.grid(column=0,row=0)

        button_yes = Button(janela,text="Yes",command=lambda:checkPassword(self,5,0,self))
        button_yes.grid(column=0,row=1)

        button_no = Button(janela,text="No",command=lambda:show_bank_menu(self))
        button_no.grid(column=0,row=2)
    else:
        texto = Label(janela,text="You dont have any bills")
        texto.grid(column=0,row=0)
        button = Button(janela,text="Enter",command=lambda:show_bank_menu(self))
        button.grid(column=0,row=1)
def loan_m(self):
    clear_window()

    texto = Label(text="How much is the value of loan: ")
    texto.grid(column=0,row=0)

    value_entry = Entry(janela)
    value_entry.grid(column=0,row=1)

    button = Button(janela,text="Enter",command=lambda:loan_terms(self,int(value_entry.get())))
    button.grid(column=0,row=2)

    quit_button = Button(janela,text="Quit",command=lambda:show_bank_menu(self))
    quit_button.grid(column=0,row=3)

def loan_terms(self,value):
    clear_window()
    texto = Label(text=f'''If you want to take out this loan, the value to be paid afterwards will be {value * 1.07}
Do you agree with that?''')
    texto.grid(column=0,row=0)

    button_yes = Button(janela,text="Yes",command=lambda:checkPassword(self,6,value,self))
    button_yes.grid(column=0,row=1)

    button_no = Button(janela,text="No",command=lambda:show_bank_menu(self))
    button_no.grid(column=0,row=2)
def update(self, subject: Subject) -> None:
    clear_window()
    if self.check:
        self.check = False
        texto = Label(janela,text="This is the news of the market")
        texto.grid(column=0,row=0)
        
        info = Label(janela,text=self.update(subject))
        info.grid(column=0,row=1)

        button = Button(janela,text="Enter",command=lambda:investiment(self))
        button.grid(column=0,row=2)
def detach_message(self,subject):
    clear_window()

    self.investiment(4,"y")

    texto = Label(janela,text="You will not receive news of investiment anymore")
    texto.grid(column=0,row=0)

    button = Button(janela,text="Enter",command=lambda:investiment(self))
    button.grid(column=0,row=1)


def investiment(self):
    if self.check:
        subject = encontrar_objeto(self._subjectlist,investiment_market)
        update(self,subject)
        return
    clear_window()
    texto = Label(text="What investiment do you want to do?")
    texto.grid(column=0,row=0)

    button1 = Button(janela,text="saving",command=lambda:saving(self,1))
    button1.grid(column=0,row=1)

    button2 = Button(janela,text="direct treasure",command=lambda:saving(self,2))
    button2.grid(column=0,row=2)

    button3 = Button(janela,text="stock exchange",command=lambda:saving(self,3))
    button3.grid(column=0,row=3)
    if self.show:
        subject = encontrar_objeto(self._subjectlist,investiment_market)
        button4 = Button(janela,text="Stop receive news",command=lambda:detach_message(self,subject))
        button4.grid(column=0,row = 4)

    quit_button = Button(janela,text="Quit",command=lambda:show_bank_menu(self))
    quit_button.grid(column=0,row=5)
def saving(self,choice):
    clear_window()
    if choice == 1:
        texto = Label(janela,text=f"With this investiment, you will have {round(self.balance * 1.0826,2)} per year, but zero risks")
        texto.grid(column=0,row=0)

        button_yes = Button(janela,text="Yes",command=lambda:agree_terms(self,1))
        button_yes.grid(column=0,row=1)
    elif choice == 2:
        texto = Label(janela,text=f"With this investiment, you will have {round(self.balance * 1.1182,2)} per year, but 2% of risks")
        texto.grid(column=0,row=0)

        button_yes = Button(janela,text="Yes",command=lambda:agree_terms(self,2))
        button_yes.grid(column=0,row=1)
    elif choice == 3:
        texto = Label(janela,text=f"With this investiment, you will have one impredictable change, high risks, but highs chance earn much money")
        texto.grid(column=0,row=0)

        button_yes = Button(janela,text="Yes",command=lambda:agree_terms(self,3))
        button_yes.grid(column=0,row=1)
    button_no = Button(janela,text="No",command=lambda:show_bank_menu(self))
    button_no.grid(column=0,row=2)
janela = Tk()

show_main_menu()

janela.mainloop()
        
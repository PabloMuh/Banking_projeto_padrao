import requests
import os
import time

class choice_class():
    def __init__(self,number) -> None:
        self.number = number
    def set(self,number):
        self.number = number
        
def convert_currency(amount, base_currency, target_currency):
    api_key = 'YOUR_EXCHANGE_RATE_API_KEY'
    endpoint = f'https://open.er-api.com/v6/latest/{base_currency}'
    
    params = {'apikey': api_key}
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'].get(target_currency)
        if rate is not None:
            converted_amount = amount * rate
            return converted_amount
        else:
            print(f"Exchange rate not available for {target_currency}.")
    else:
        print(f"Failed to fetch exchange rate. Status code: {response.status_code}")
        
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Now you have Downloaded the cheque book")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def agree_terms():
    print("To make this investment, you will have to agree to make your data and transactions available, for constant updating of your personal and market financial situation.")
    choice = input("Press y for yes and anything for no: ")
    choice = choice.lower()
    if choice == "y":
        return True
    else:
        return False
def check_instance(lista,MinhaClasse):
    nao_contem_minha_classe = True
    for elemento in lista:
        if isinstance(elemento, MinhaClasse):
            nao_contem_minha_classe = False
            break
    return nao_contem_minha_classe
def encontrar_objeto(lista, classe):
    for elemento in lista:
        if isinstance(elemento, classe):
            return elemento
    return None

from operations import *
from Subject import *

url = 'https://static.vecteezy.com/system/resources/thumbnails/004/566/136/small/bank-check-cheque-template-free-vector.jpg'
filename = 'cheque.jpg'
class access_account(account):
    def __init__(self, code, password):
        super().__init__(code, password)
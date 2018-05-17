class Account:
    num_accounts = 0
    def __init__(self, name):
        self.name = name
        Account.num_accounts +=1
    def __del__(self):
        Account.num_accounts -=1



kim  = Account('kim')
lee = Account('lee')

print(kim.name)
print(lee.name)
print(kim.num_accounts)
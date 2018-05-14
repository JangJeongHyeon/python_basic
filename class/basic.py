class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    def show_info(self):
        print('-'*30)
        print('Name: ', self.name)
        print('E-mail: ', self.email)
        print('Address: ', self.addr)
        print('-'*30)



val = BusinessCard()
val.set_info('JohnMark','practice1356@gmail.com','Anseong')
print(val)
print()
val.show_info()
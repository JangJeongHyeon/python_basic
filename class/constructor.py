class BusinessCard:
    def __init__(self):
        self.name = 'empty'
        self.email = 'empty'
        self.addr = 'empty'
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


card = BusinessCard()
card.show_info()
card.set_info('JohnMark','practice1356@gmail.com','Anseong')
card.show_info()
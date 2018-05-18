class Contact:
    def __init__(self, name, phone_number, e_mail, address):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.address = address

    def print_info(self):
        print('Name: ', self.name)
        print('Phone Number: ', self.phone_number)
        print('E-mail: ', self.e_mail)
        print('Address: ', self.address)

# add
def new_contact():
    name = input('Name: ')
    phone_number = input('Phone Number: ')
    e_mail = input('E-mail: ')
    address = input('Address: ')
    return Contact(name, phone_number, e_mail,address)

def run():
    # kim = Contact('JohnMark','010-1234-1234','practice1356@gmail.com','Anseong')
    # kim.print_info()
    contact = new_contact()
    contact.print_info()

    
if __name__ == '__main__':
    run()

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

""" create new contact class instance """
def new_contact():
    name = input('Name: ')
    phone_number = input('Phone Number: ')
    e_mail = input('E-mail: ')
    address = input('Address: ')
    return Contact(name, phone_number, e_mail,address)

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu = input("메뉴선택: ")
    return int(menu)


def run():
    while True:
        menu = print_menu()
        if menu == 4:
            break

    
if __name__ == '__main__':
    run()

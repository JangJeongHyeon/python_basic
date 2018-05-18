import os


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
    return Contact(name, phone_number, e_mail, address)


def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu = input("메뉴선택: ")
    return int(menu)


def store_contact(contact_list):
    path = os.getcwd()
    file = open(path+'/project/contact/contact_db.txt', 'wt')
    for contact in contact_list:
        file.write(contact.name+'\n')
        file.write(contact.phone_number+'\n')
        file.write(contact.e_mail+'\n')
        file.write(contact.address+'\n')
    file.close()


def load_contactdb(contact_list):
    path = os.getcwd()
    file = open(path+'/project/contact/contact_db.txt', 'rt')
    lines = file.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        address = lines[4*i+3].rstrip('\n')
        contact_list.append(Contact(name, phone, email, address))
    file.close()


def run():
    contact_list = []
    while 1:
        menu = print_menu()
        if(menu == 1):
            contact = new_contact()
            contact_list.append(contact)
        elif(menu == 2):
            for contact in contact_list:
                print("="*20)
                contact.print_info()
                print("="*20)
        elif(menu == 3):
            name = input("이름: ")
            for index, item in enumerate(contact_list):
                if(item.name == name):
                    del contact_list[index]
        elif(menu == 4):
            store_contact(contact_list)
            break


if __name__ == '__main__':
    run()

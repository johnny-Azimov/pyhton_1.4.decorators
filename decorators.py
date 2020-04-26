# 1.Написать декоратор - логгер.

import datetime


class logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.ret = self.func(*args, **kwargs)
        with open('logger.txt', 'a', encoding='utf-8') as f:
            f.write(f'{datetime.datetime.now()} вызов {self.func.__name__} \
                функции с позиционными {self.args} и ключевыми аргументами {self.kwargs} \
                возвращенными {self.ret} \n ')
        return self.ret


# 2.Написать декоратор из п.1, но с параметром – путь к логам.

def parameter_logger(file_name):
    def wrapper(func):
        def former(*args, **kwargs):
            time = datetime.datetime.now()
            ret = func(*args, **kwargs)
            str = f'{time} вызов {func.__name__} с {args} {kwargs} возвратом {ret} \n'
            with open(file_name, 'a', encoding='utf-8') as f:
                f.write(str)
            return ret
        return former
    return wrapper

# 3.Применить написанyый логгер к приложению из любого предыдущего д/з.


class Contact:

    def __init__(self, name, surname, number, favorite_contact=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.favorite_contact = favorite_contact
        self.args = args
        self.kwargs = kwargs
        for passion in self.args:
            print('-', passion)

    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n' \
               f'Номер телефона: {self.number}\n' \
               f'В Избранных: {self.favorite_contact}\n' \
               f'Дополнительная информация: \n\t{self.kwargs}'


jhon = Contact('Jhon', 'Smith', '+71234567809',
               telegram='@jhony', email='jhony@smith.com')
Heisenberg = Contact('Walter', 'White', '+15467770102',
                     telegram='@heisenberg', email='walter@white.com')
# print(jhon)


class Phonebook:

    def __init__(self, book_name):
        self.contact_list = []
        self.book_name = book_name

    @parameter_logger('test.txt')
    def add_contact(self, contact_inatance):
        self.contact_list.append(contact_inatance)

    @parameter_logger('test.txt')
    def print_contacts(self):
        for contact in self.contact_list:
            print(contact)

    @parameter_logger('test.txt')
    def find_contact(self):
        name_2 = input('Введите имя: ')
        family_2 = input('Введите фамилию: ')
        for contact in self.contact_list:
            if contact.name == name_2:
                if contact.surname == family_2:
                    print(contact)
                else:
                    print('Контакт не найден')
                    break

    @parameter_logger('test.txt')
    def remove_contacts(self):
        rem_contact_number = input('Введите номер контакта для удаления: ')
        for contact in self.contact_list:
            if contact.number == rem_contact_number:
                self.contact_list.remove(contact)
                print(f'Контакст {contact.name} удален')

    @parameter_logger('test.txt')
    def find_priority_numbers(self):
        for contact in self.contact_list:
            if contact.favorite_contact != False:
                print(
                    f'{contact.name}\nИзбранные номера: {contact.favorite_contact}')


MyBook = Phonebook('MyBook')
MyBook.add_contact(jhon)
MyBook.add_contact(Heisenberg)


@parameter_logger('test.txt')
def main():
    while True:
        print(f'Спмсок доступных функций:\n'
              f'1 - Вывод всех контактов \n'
              f'2 - Поиск контакта по имени и фамилии\n'
              f'3 - Вывод всех избрвнных номеров\n'
              f'4 - Удаление контакта\n'
              f'5 - Выход')
        user_input = input('Введите команду: ')
        if user_input == '1':
            MyBook.print_contacts()
            print(input())
        elif user_input == '2':
            MyBook.find_contact()
            print(input())
        elif user_input == '3':
            MyBook.find_priority_numbers()
            print(input())
        elif user_input == '4':
            MyBook.remove_contacts()
            print(input())
        elif user_input == '5':
            break


if __name__ == '__main__':
    main()

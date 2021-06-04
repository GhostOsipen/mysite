import pickle
import click
import os.path
from prettytable import PrettyTable

class Person:
    def __init__(self,  name, second_name, phone) -> None:
        self.name = name
        self.phone = phone
        self.second_name = second_name

        print(f"{self.name} ADDED")

    def __del__(self) -> None:
        pass

class PhoneBook:
    d = {}

    @classmethod
    def add_person(cls, name: str, second_name: str, phone: str):
        if name in cls.d.keys():
            print(f"Person [{name}] already exist")
        else:
            person = Person(name, second_name, phone)
            cls.d[person.name] = person

    @classmethod
    def delete_person_by_name(cls, name: str):
        del cls.d[name]
        print(name, "DELETED")

    @classmethod
    def change_person_name(cls, old_name, new_name):
        cls.d[old_name].name = new_name
        cls.d[new_name] = cls.d[old_name]
        del cls.d[old_name]
        print("CHANGED")

    @classmethod
    def change_person_second_name(cls, name, new_second_name):
        cls.d[name].second_name = new_second_name
        print("CHANGED")

    @classmethod
    def change_person_phone(cls, name, new_phone):
        cls.d[name].phone = new_phone
        print("CHANGED")

    @classmethod
    def person_list(cls):
        x = PrettyTable()
        x.field_names = ["Name","Last Name","Phone"]
        for person in cls.d.values():
            x.add_row([person.name,person.second_name,person.phone])
            #print(f"Name: {person.name}, Second name: {person.second_name}, Phone: {person.phone}")
        print(x)

    @classmethod
    def find_person(cls, s):
        x = PrettyTable()
        x.field_names = ["Name","Last Name","Phone"]
        for person in cls.d.values():
            if (s.lower() in person.name.lower()) or (s.lower() in person.second_name.lower()) or (s.lower() in person.phone.lower()):
                x.add_row([person.name,person.second_name,person.phone])
                #print(f"Name: {person.name}, Second name: {person.second_name}, Phone: {person.phone}")
        print(x)

def creating():
    print("creating data.pickle...")
    with open('data.pickle', 'wb') as f:
        pickle.dump(PhoneBook.d, f)

def saving():
    print("save to data.pickle...")
    with open('data.pickle', 'wb') as f:
        pickle.dump(PhoneBook.d, f)

def loading():
    print("load from data.pickle...")
    with open('data.pickle', 'rb') as f:
        PhoneBook.d = pickle.load(f)

#==========================================================================================================
# @click.group()
# def main():
#     pass

# @click.group()
# def cli():
#     pass

# @main.command()
# def table():
#     PhoneBook.person_list()

# @main.command()
# @click.argument('name')
# @click.argument('second_name')
# @click.argument('phone')
# def add(name, second_name, phone):
#     PhoneBook.add_person(name,second_name,phone)
#     saving()

# @main.command()
# @click.argument("name")
# def delete(name):
#     PhoneBook.delete_person_by_name(name)
#     saving()

# @main.command()
# @click.argument("name")
# def change(name):
#     if name not in PhoneBook.d.keys():
#         print("person don't exist")
#     else:
#         print('''
# name
# second name
# phone
# ''')
#         value = click.prompt("What change?")
#         if value == "name":
#             old_name = PhoneBook.d[name].name
#             new_name = click.prompt("New name")
#             PhoneBook.change_person_name(old_name, new_name)
#             saving()
#         elif value == "second name":
#             name = PhoneBook.d[name].name
#             new_second_name = click.prompt("New second name")
#             PhoneBook.change_person_second_name(name, new_second_name)
#             saving()
#         elif value == "phone":
#             name = PhoneBook.d[name].name
#             new_phone = click.prompt("New phone")
#             PhoneBook.change_person_phone(name, new_phone)
#             saving()

# @main.command()
# @click.argument("value")
# def find(value):
#     PhoneBook.find_person(value)

# cli.add_command(table)
# cli.add_command(add)
# cli.add_command(delete)
# cli.add_command(change)
# cli.add_command(find)

#==========================================================================================================
if os.path.isfile('data.pickle'):
    loading() #load data
else:
    creating()

# if __name__ == '__main__':
#     main()
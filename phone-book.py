import pickle
import re
from typing import Dict
from flask import Flask, redirect, url_for, request, render_template
from flask_table import Table, Col
app = Flask(__name__)


class Person:
    def __init__(self,  name, second_name, phone) -> None:
        self.name = name
        self.second_name = second_name
        self.phone = phone

        print(f"{self.name} ADDED")

    def __del__(self) -> None:
        pass


class PhoneBook:
    book = {}

    @classmethod
    def add_person(cls, name: str, second_name: str, phone: str):
        if phone in cls.book.keys():
            print(f"Person [{phone}] already exist")
        else:
            person = Person(name, second_name, phone)
            cls.book[person.phone] = person

    @classmethod
    def delete_person(cls, phone: str):
        del cls.book[phone]
        print("DELETED")

    @classmethod
    def change_person_name(cls, phone, new_name):
        cls.book[phone].name = new_name
        print("CHANGED")

    @classmethod
    def change_person_second_name(cls, phone, new_second_name):
        cls.book[phone].second_name = new_second_name
        print("CHANGED")

    @classmethod
    def change_person_phone(cls, old_phone, new_phone):
        cls.book[old_phone].phone = new_phone
        cls.book[new_phone] = cls.book[old_phone]
        del cls.book[old_phone]
        print("CHANGED")

    @classmethod
    def person_list(cls):
        for person in cls.book.values():
            print(
                f"Name: {person.name}, Second name: {person.second_name}, Phone: {person.phone}")

    @classmethod
    def find_person(cls, s) -> Dict:
        temp_dict = {}
        for person in cls.book.values():
            if (s.lower() in person.name.lower()) or (s.lower() in person.second_name.lower()) or (s.lower() in person.phone.lower()):
                print(
                    f"Name: {person.name}, Second name: {person.second_name}, Phone: {person.phone}")
                temp_dict[person.phone] = person
        return temp_dict


def create_pickle():
    print("creating data.pickle...")
    with open('data.pickle', 'wb') as f:
        pickle.dump(PhoneBook.book, f)


def save_pickle():
    print("save to data.pickle...")
    with open('data.pickle', 'wb') as f:
        pickle.dump(PhoneBook.book, f)


def load_pickle():
    print("load from data.pickle...")
    with open('data.pickle', 'rb') as f:
        PhoneBook.book = pickle.load(f)


# ===================================================================
load_pickle()


@app.route('/')
def main():
    return redirect(url_for('table'))


@app.route('/table', methods=['POST', 'GET'])
def table():
    if request.method == "POST":
        return redirect(url_for('find', find_name=request.form['find_name']))
    return render_template('table.html', table=PhoneBook.book)


@app.route('/table/<find_name>', methods=['POST', 'GET'])
def find(find_name):
    if request.method == "POST":
        return redirect(url_for('table'))
    return render_template('find.html', table=PhoneBook.find_person(find_name))


@app.route('/table/add', methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        PhoneBook.add_person(
            request.form['name'], request.form['sname'], request.form['phone'])
        save_pickle()
        return redirect(url_for('table'))
    return render_template('add.html')


@app.route('/table/edit/<key>', methods=['POST', 'GET'])
def edit(key):
    if request.method == "POST":
        if request.form['name'] != PhoneBook.book[key].name:
            PhoneBook.change_person_name(key, request.form['name'])
        if request.form['sname'] != PhoneBook.book[key].second_name:
            PhoneBook.change_person_second_name(key, request.form['sname'])
        if request.form['phone'] != PhoneBook.book[key].phone:
            PhoneBook.change_person_phone(key, request.form['phone'])
        save_pickle()
        return redirect(url_for('table'))
    return render_template('edit.html', table=PhoneBook.book,
                           name=PhoneBook.book[key].name,
                           sname=PhoneBook.book[key].second_name,
                           phone=PhoneBook.book[key].phone)


@app.route('/table/delete/<key>', methods=['POST', 'GET'])
def delete(key):
    if request.method == "POST":
        PhoneBook.delete_person(key)
        save_pickle()
    return redirect(url_for('table'))


if __name__ == '__main__':
    app.run(debug=True)

from collections import UserDict
from datetime import datetime
import re


class Field:
    def __init__(self, value):
        self.value = value


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.get_value = value

    @property
    def get_value(self):
        return self.value

    @get_value.setter
    def get_value(self, value):
        pattern = "\d\d.\d\d.\d{4}"
        if value == re.search(pattern, value).group():
            self.value = datetime.strptime(value, "%d.%m.%Y")
        else:
            raise Exception("Please give correct date")


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.get_value = value

    @property
    def get_value(self):
        return self.value

    @get_value.setter
    def get_value(self, value):
        if type(value) == str:
            self.value = value
        else:
            raise TypeError('Name must be str type')


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.get_value = value

    @property
    def get_value(self):
        return self.value

    @get_value.setter
    def get_value(self, value):
        if value.isdigit():
            self.value = value
        else:
            raise Exception('Phone not correct')


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name
        self.phones = []
        self.birthday = birthday

        if phone:
            self.phones.append(phone)

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if new_phone.value not in [ph.value for ph in self.phones]:
            self.phones.append(new_phone)

    def delete_phone(self, phone):
        for ph in self.phones:
            if phone == ph.value:
                self.phones.remove(ph)

    def change_phone(self, old_phone, new_phone):
        for ph in self.phones:
            if old_phone == ph.value:
                self.delete_phone(old_phone)
                self.add_phone(new_phone)

    def days_to_birthday(self):
        today = datetime.now()
        birthday = self.birthday.value
        days_to_birthday = (birthday - today).days
        if days_to_birthday < 0:
            birthday = birthday.replace(year=today.year + 1)
            days_to_birthday = (birthday - today).days
            return days_to_birthday
        return days_to_birthday


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self, quantity):
        return Iterator(quantity)


class Iterator:
    def __init__(self, quantity):
        self.quantity = quantity
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start <= self.quantity:
            return self
        else:
            raise StopIteration

""" Как сделать метод ierator что бы возвращал генератор вообще не пойму"""

# if __name__ == '__main__':
#     name = Name('Bill')
#     phone = Phone('1234567890')
#     birth = Birthday('11.05.1995')
#     rec = Record(name, phone, birth)
#
#     ab = AddressBook()
#     ab.add_record(rec)
#     name = Name('Seee')
#     phone = Phone('989898989')
#     birth = Birthday('20.11.1995')
#     rec = Record(name, phone, birth)
#     ab.add_record(rec)
#     print(ab.data[name.value].birthday.value)
#     print(ab)
#     for i in ab.iterator(1):
#         print(i)

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

    def __str__(self):
        return f"{self.name.value} {[ph.value for ph in self.phones]} {self.birthday.value.date()}"


class AddressBook(UserDict):
    N = 0

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self, n=None):
        if n:
            AddressBook.N = n
        return self.__next__()

    def __iter__(self):
        temp_lst = []
        counter = 0

        for var in self.data.values():
            temp_lst.append(var)
            counter += 1
            if counter >= AddressBook.N:
                yield temp_lst
                temp_lst.clear()
                counter = 0
        yield temp_lst

    def __next__(self):
        generator = self.__iter__()
        page = 1
        while True:
            user_input = input("Press ENTER")
            if user_input == "":
                try:
                    result = next(generator)
                    if result:
                        print(f"{'*' * 20} Page {page} {'*' * 20}")
                        page += 1
                    for var in result:
                        print(var)
                except StopIteration:
                    print(f"{'#' * 20} END {'#' * 20}")
                    break
            else:
                break


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    birth = Birthday('11.05.1995')
    rec = Record(name, phone, birth)

    ab = AddressBook()
    ab.add_record(rec)

    name1 = Name('Seee1')
    phone1 = Phone('989898989')
    birth1 = Birthday('20.11.1995')
    rec1 = Record(name1, phone1, birth1)

    name2 = Name('Seee2')
    phone2 = Phone('989898989')
    birth2= Birthday('20.11.1995')
    rec2 = Record(name2, phone2, birth2)

    name3 = Name('Seee3')
    phone3 = Phone('989898989')
    birth3 = Birthday('20.11.1995')
    rec3 = Record(name3, phone3, birth3)

    name4 = Name('Seee4')
    phone4 = Phone('989898989')
    birth4 = Birthday('20.11.1995')
    rec4 = Record(name4, phone4, birth4)

    ab.add_record(rec1)
    ab.add_record(rec2)
    ab.add_record(rec3)
    ab.add_record(rec4)
    print(ab.data[name.value].birthday)
    print(ab.iterator(5))
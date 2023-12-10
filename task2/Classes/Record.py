import Name
from task2.Classes import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        if Phone.validate_phone_number(number):
            self.phones.append(Phone(number))
        else:
            raise ValueError("Invalid phone number format. It should have 10 digits.")
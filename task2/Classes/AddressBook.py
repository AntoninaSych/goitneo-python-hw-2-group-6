from task2.Decorators.DecoratorsError import input_error, contact_not_found_error
class AddressBook:
    def __init__(self):
        self.records = {}

    @input_error
    def add_record(self, record):
        self.records[record.name.name] = record

    @contact_not_found_error
    def find(self, name):
        return self.records.get(name)

    @contact_not_found_error
    def delete(self, name):
        if name in self.records:
            del self.records[name]
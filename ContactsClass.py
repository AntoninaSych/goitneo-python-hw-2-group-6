from InputError import input_error, contact_not_found_error
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    @input_error
    def add_contact(self, name, phone, email, favorite):
        try:
            self.contacts.append(
                {
                    "id": Contacts.current_id,
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "favorite": favorite,
                }
            )
            Contacts.current_id += 1
            return "Contact added."
        except ValueError:
            return "Please provide name and phone please."

    @contact_not_found_error
    def get_contact(self, contact_id):
        try:
            contact_id = int(contact_id)
            contact = next((c for c in self.contacts if c["id"] == contact_id), None)
            if contact:
                return f"Contact ID: {contact['id']}\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nFavorite: {contact['favorite']}"
            else:
                return "Contact not found."
        except ValueError:
            return "Invalid input. Enter a valid contact ID."

    @contact_not_found_error
    def remove_contact(self, contact_id):
        try:
            contact_id = int(contact_id)
            contact = next((c for c in self.contacts if c["id"] == contact_id), None)
            if contact:
                self.contacts.remove(contact)
                return "Contact deleted."
            else:
                return "Contact not found."
        except ValueError:
            return "Invalid input. Please enter a valid contact ID."
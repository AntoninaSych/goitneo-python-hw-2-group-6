class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

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
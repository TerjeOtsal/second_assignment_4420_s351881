# contacts_manager.py

class ContactsManager:
    """
    A class to manage a list of predefined contacts.
    
    Attributes:
        contacts (list): A list of dictionaries representing the predefined contacts.
    """

    def __init__(self):
        """Initializes the ContactsManager with a predefined list of contacts."""
        self.contacts = [
            {"name": "Alice", "email": "alice@example.com", "preferred_time": "08:00 AM"},
            {"name": "Bob", "email": "bob@example.com", "preferred_time": "09:00 AM"},
            {"name": "Charlie", "email": "charlie@example.com", "preferred_time": "07:30 AM"}
        ]

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        """
        Adds a new contact to the list.
        """
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)

    def remove_contact(self, name):
        """
        Removes a contact from the list based on the given name.
        """
        self.contacts = [c for c in self.contacts if c['name'] != name]

    def get_contacts(self):
        """
        Retrieves the list of contacts.
        """
        return self.contacts

    def list_contacts(self):
        """
        Prints all contacts in a readable format.
        """
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")

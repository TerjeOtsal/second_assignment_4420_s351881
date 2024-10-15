# contacts.py

class Contacts:
    """
    A class to manage the list of friends for sending personalized 'Good Morning' messages.
    """

    def __init__(self):
        """Initializes an empty list of contacts."""
        self.contacts = []

    def add_contact(self, name, contact_info, preferred_time="08:00 AM"):
        """
        Adds a new contact to the list of contacts.
        """
        contact = {
            'name': name,
            'contact_info': contact_info,
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

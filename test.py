import unittest
from morning_greetings.contacts import Contacts
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message

class TestMorningGreetings(unittest.TestCase):

    def setUp(self):
        self.contacts = Contacts()
        self.contacts.add_contact("Terje Saltskår", "terje@example.com", "08:00 AM")

    def test_add_contact(self):
        """Test adding a new contact."""
        self.contacts.add_contact("Jane Doe", "jane@example.com", "09:00 AM")
        contacts_list = self.contacts.get_contacts()
        self.assertEqual(len(contacts_list), 2)
        self.assertEqual(contacts_list[1]['name'], "Jane Doe")

    def test_remove_contact(self):
        """Test removing a contact."""
        self.contacts.remove_contact("Terje Saltskår")
        contacts_list = self.contacts.get_contacts()
        self.assertEqual(len(contacts_list), 0)

    def test_generate_message(self):
        """Test message generation."""
        message = generate_message("Terje")
        self.assertEqual(message, "Good Morning, Terje! Have a great day!")

    def test_send_message(self):
        """Test message sending simulation."""
        with self.assertRaises(ValueError):
            send_message("", "Test Message")  # Missing email should raise an error

if __name__ == "__main__":
    unittest.main()
# main.py

from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message

def main():
    """
    Main function to automate the process of sending personalized 'Good Morning' messages.
    Steps:
    1. Retrieve a list of contacts.
    2. Generate a personalized message for each contact.
    3. Simulate sending the message.
    4. Log the sent message to a file.
    """
    # Step 1: Initialize ContactsManager and retrieve contacts
    contacts_manager = ContactsManager()
    contacts = contacts_manager.get_contacts()

    # Step 2: Generate and send messages for each contact
    for contact in contacts:
        # Generate a personalized message
        message = generate_message(contact['name'])
        
        # Simulate sending the message
        send_message(contact['email'], message)
        
        # Log the message
        log_message(contact, message)

if __name__ == "__main__":
    main()

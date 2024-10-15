import schedule
import time
from datetime import datetime
from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message


def send_morning_messages():
    """
    Function to automate the process of sending personalized 'Good Morning' messages.
    Steps:
    1. Retrieve a list of contacts.
    2. Generate a personalized message for each contact.
    3. Simulate sending the message.
    4. Log the sent message to a file.
    """
    try:
        # Step 1: Initialize ContactsManager and retrieve contacts
        contacts_manager = ContactsManager()
        contacts = contacts_manager.get_contacts()

        if not contacts:
            raise ValueError("No contacts available to send messages to.")

        # Step 2: Generate and send messages for each contact
        for contact in contacts:
            try:
                # Generate a personalized message
                message = generate_message(contact['name'])
                
                # Simulate sending the message
                send_message(contact['email'], message)
                
                # Log the message
                log_message(contact, message)
            except ValueError as ve:
                print(f"Error sending message to {contact['name']}: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred for {contact['name']}: {e}")

    except Exception as e:
        print(f"An error occurred while processing the contacts: {e}")

def schedule_morning_greetings(time_str):
    """
    Schedule the send_morning_messages function to run at the specified time every day.
    
    Args:
        time_str (str): Time in 24-hour format (e.g., '08:00' for 8:00 AM).
    """
    schedule.every().day.at(time_str).do(send_morning_messages)
    print(f"Scheduled morning messages to be sent every day at {time_str}.")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Example: Schedule the messages to be sent at 08:00 AM every day
    schedule_morning_greetings("22:46")

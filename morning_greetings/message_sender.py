# message_sender.py

def send_message(contact_info, message):
    """
    Simulates sending a message to a given contact.
    """
    if not contact_info:
        raise ValueError("Contact information is missing")

    # Simulate sending a message by printing
    print(f"Sending message to {contact_info}: {message}")

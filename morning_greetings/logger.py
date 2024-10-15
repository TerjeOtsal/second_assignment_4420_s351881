# logger.py

import datetime

def log_message(contact, message):
    """
    Logs the details of a sent message to a text file named 'message_log.txt'.
    """
    with open("message_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']}: {message}\n")

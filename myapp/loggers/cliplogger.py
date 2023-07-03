import threading
import time
import datetime
import pyperclip
from myapp.db.db import Database
from myapp.encryption.encryption import encrypt_data


class ClipLogger:
    def __init__(self, user_id):
        self.user_id = user_id
        self.last_clipboard_content = None
        self._stop_event = threading.Event() 

    def start(self):
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def _run(self):
        db = Database()
        while not self._stop_event.is_set():
            clipboard_content = pyperclip.paste()
            if clipboard_content != self.last_clipboard_content:
                encrypted_content = encrypt_data(clipboard_content.encode())
                db.insert_clip_log(self.user_id, encrypted_content, datetime.datetime.now())
                self.last_clipboard_content = clipboard_content
            time.sleep(1)

    def stop(self):
        self._stop_event.set()  
        self.thread.join()  # Wait for the logging thread to finish


# In this revised version of ClipLogger, the clipboard content is no longer written to a text file. Instead, it is encrypted using the encrypt function from encryption.py and then stored in the database.

# The ClipLogger now takes a user_id as an argument when it is instantiated. This is used to associate the clipboard content with a particular user when it is stored in the database.

# The start method now contains a loop that continuously checks the clipboard for new content. If new content is found, it is encrypted and stored in the database, associated with the current user's ID.

# A new Database instance is created at the beginning of the start method. This instance is used to interact with the database.

# Remember, the ClipLogger now requires a user ID to be provided when it's instantiated. This ID should be the ID of the currently logged-in user.

# This code does not handle the case where the application
# In this code:

# The ClipLogger class now has a _stop_event attribute, which is an instance of threading.Event.
# The while loop in the start method now only runs while the _stop_event is not set.
# A stop method has been added to the ClipLogger class. This method sets the _stop_event, ending the while loop in the start method.
# You can call ClipLogger.stop() to stop the logging when the application is about to shut down. Make sure to run the ClipLogger.start() method in a separate thread, so that it doesn't block the rest of your application.
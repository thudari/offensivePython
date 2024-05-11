import socket
import ssl
import os
from datetime import datetime
import asyncio
import requests

def create_tls_server(host, port):
    """ Creates a TLS server that listens for connections. """
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)  # Paths to certificates
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    ssock = context.wrap_socket(sock, server_side=True)

    return ssock

def receive_file(connection, file_path):
    """ Receives a file over a TLS socket and saves it to a specified path. """
    with open(file_path, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)

def handle_client(connection):
    """ Handles a client connection: receives a file and saves it. """
    print("Client connected.")
    try:
        # Gets the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Build the full path where the file will be saved with the timestamp
        file_path = os.path.join(os.getcwd(), f'received_file_{timestamp}.zip')
        receive_file(connection, file_path)
        print(f"File received and saved in {file_path}.")
        # Here you can add more logic to process the file - Example: telegram bot notifies
        asyncio.run(send_notification(file_path))
    finally:
        connection.close()

async def send_notification(file_path):
    message = f"New file received\nName: {file_path}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHATID, "text": message}
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
    except Exception as e:
        print(f"Error sending message: {e}")

def main():
    host = ''  # Server address
    port = 4444  # Server port
    server_socket = create_tls_server(host, port)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            client_connection, _ = server_socket.accept()
            handle_client(client_connection)
    except KeyboardInterrupt:
        print("Servidor encerrando.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    CERTFILE = 'server.crt' 
    KEYFILE = 'server.key'
    TOKEN = '' # Telegram token
    CHATID = '' # Telegram chatID
    main()

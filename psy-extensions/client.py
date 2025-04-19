#import modules
import socket
import json
import struct
import os

#setup variables
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

#startup functions
def send_message(sock):
    message = input("Enter message: ")
    header = {
        'type': 'message',
        'size': len(message.encode('utf-8'))
    }
    send_data(sock, header, message.encode('utf-8'))

def send_file(sock):
    filepath = input("Enter file path: ")
    if not os.path.exists(filepath):
        print("File not found")
        return
    
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        file_data = f.read()
    
    header = {
        'type': 'file',
        'size': len(file_data),
        'filename': filename
    }
    send_data(sock, header, file_data)
    print(f"File '{filename}' sent")

def send_data(sock, header, data):
    try:
        header_bytes = json.dumps(header).encode('utf-8')
        header_length = struct.pack('!I', len(header_bytes))
        sock.sendall(header_length)
        sock.sendall(header_bytes)
        sock.sendall(data)
    except Exception as e:
        print(f"Error sending data: {e}")

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to server")
        print(""
        "\nmessage - Sends a message"
        "\nfile - Sends a file"
        "\nexit - Exits the client")
        while True:
            choice = input("Choose option: ")
            if choice == 'message':
                send_message(s)
            elif choice == 'file':
                send_file(s)
            elif choice == 'exit':
                break
            else:
                print("Invalid choice")

#main function
if __name__ == "__main__":
    start_client()
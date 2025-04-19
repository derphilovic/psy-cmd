#import modules
import socket
import threading
import json
import struct
import os

#setup variables
HOST = '0.0.0.0'
PORT = 65432

#starttup functions
def recv_all(sock, size):
    data = b''
    while len(data) < size:
        chunk = sock.recv(min(size - len(data), 4096))
        if not chunk:
            break
        data += chunk
    return data

def handle_client(sock):
    try:
        while True:
            # Read header length (4 bytes)
            header_length_bytes = sock.recv(4)
            if len(header_length_bytes) < 4:
                print("Client disconnected.")
                break
            header_len = struct.unpack('!I', header_length_bytes)[0]

            # Read header
            header_bytes = recv_all(sock, header_len)
            if not header_bytes:
                print("Connection closed during header.")
                break
            header = json.loads(header_bytes.decode('utf-8'))

            data_size = header['size']
            
            # Receive data
            data = recv_all(sock, data_size)
            if len(data) != data_size:
                print("Incomplete data received.")
                continue

            if header['type'] == 'message':
                print(f"\nReceived message: {data.decode('utf-8')}")
            elif header['type'] == 'file':
                filename = header['filename']
                with open(filename, 'wb') as f:
                    f.write(data)
                print(f"\nFile '{filename}' received ({data_size} bytes)")
            else:
                print("\nUnknown data type")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            client_thread = threading.Thread(target=handle_client, args=(conn,))
            client_thread.start()

#main functions
if __name__ == "__main__":
    start_server()

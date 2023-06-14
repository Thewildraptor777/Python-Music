import socket
import os
def send_files():
    # Replace the IP address and port number with those of the receiving computer
    ip_address = "192.168.1.72"
    port = 5555

    # Replace the folder path with the path of the folder containing the files you want to transfer
    folder_path = "C:\\Code\\Repos\\Python Music\\data\\audio"

    # Create a socket object and connect to the receiving computer
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_address, port))

    # Loop through all the files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Open the file and read its contents
        with open(file_path, "rb") as f:
            file_contents = f.read()

        # Send the file name and contents over the socket connection
        sock.sendall(filename.encode())
        sock.sendall(file_contents)

    # Send a signal to indicate that all files have been sent
    sock.sendall("EOF".encode())

    # Close the socket connection
    sock.close()
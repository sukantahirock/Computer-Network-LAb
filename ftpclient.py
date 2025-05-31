# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:13:18 2023

@author: USER
"""
import socket

def receive_file(connection, filename):
    try:
        with open(filename, 'wb') as file:
            data = connection.recv(1024)
            while data:
                file.write(data)
                data = connection.recv(1024)
    except Exception as e:
        print(f"Error receiving file: {str(e)}")

def main():
    server_ip = '127.0.0.1'
    server_port = 1000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f"Server listening on {server_ip}:{server_port}")

    while True:
        try:
            connection, address = server_socket.accept()
            print(f"Accepted connection from {address}")
            
            # Specify the full path where you want to save the received file
            receive_file(connection, "C:/Users/USER/.spyder-py3/received.txt")
            print("accepted");
            connection.close()
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

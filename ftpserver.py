# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:14:18 2023

@author: USER
"""
import tkinter as tk
from tkinter import filedialog
import socket

def send_file(file_path):
    server_ip = '127.0.0.1'
    server_port = 1000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

    client_socket.close()

if __name__ == "__main__":
    root = tk.Tk()
    
    # Open a file dialog for the user to select a file
    selected_file_path = filedialog.askopenfilename()
    
    # Close the tkinter root window
    root.destroy()

    if selected_file_path:
        print("Selected file:", selected_file_path)
        send_file(selected_file_path)
    else:
        print("No file selected.")

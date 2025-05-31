import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)

client_socket.connect(server_address)

while True:
    message = input("Enter a message to send to the server or write 'exit' to quit: ")
    if message.lower() == 'exit':
        break
    

    # Send the message to the server
    client_socket.send(message.encode())

    # Receive and display the server's response
    response = client_socket.recv(1024)
    print(f"Server response: {response.decode()}")

# Close the client socket
client_socket.close()

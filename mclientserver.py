import pyfiglet 
import socket
import threading

text = pyfiglet.figlet_format("ZWN _ CRAWL")
print(text)

def handle_client(connection, address):
    # Receive prompt for username
    username_prompt = " [+]Enter your username: "
    connection.sendall(bytes(username_prompt, "utf-8"))

    # Receive username from client
    username = connection.recv(1024).decode("utf-8")
    print("Member joined\n", username)

    # Start receiving and sending messages
    while True:
        try:
            message = connection.recv(1024).decode("utf-8")
            if not message:
                break
            print(username + ":", message)
            reply = input(" [+]Your reply: ")
            connection.sendall(bytes(reply, "utf-8"))
        except KeyboardInterrupt:
            print(">Exiting<")
            break

    connection.close()

def main():
    host = input(" [+]Enter server IP address: ")  # Server IP address input from user
    port = int(input(" [+]Enter server port number: "))  # Server port number input from user

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for incoming connections, allowing up to 5 queued connections

    print(" >Server is listening on", host + ":" + str(port))

    while True:
        try:
            connection, address = server_socket.accept()  # Accept incoming connection
            print(">Connected to:", address)

            # Start a new thread to handle the client connection
            client_thread = threading.Thread(target=handle_client, args=(connection, address))
            client_thread.start()
        except KeyboardInterrupt:
            print(">Exiting<")
            break

    server_socket.close()

if __name__ == "__main__":
    main()

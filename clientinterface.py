import socket
import pyfiglet
text = pyfiglet.figlet_format("ZWN _ CRAWL")
print(text)

def main():
   
    server_ip = input(" [+]Enter server IP address: ")  # Server IP address input from user
    port = int(input(" [+]Enter server port "))  # Server port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    # Receive prompt for username
    username_prompt = client_socket.recv(1024).decode("utf-8")
    print(username_prompt, end="")
    username = input()

    # Send username to server
    client_socket.send(bytes(username, "utf-8"))

    # Start receiving and sending messages
    while True:
        try:
            message = input("Your message: ")
            client_socket.send(bytes(message, "utf-8"))
            reply = client_socket.recv(1024).decode("utf-8")
            print(" >Received reply:", reply)
        except KeyboardInterrupt:
            print("\n Exiting...")
            break

    client_socket.close()

if __name__ == "__main__":
    main()

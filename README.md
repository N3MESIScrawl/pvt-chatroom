# ZWN CRAWL Chatroom

ZWN CRAWL Chatroom is a Python-based chat application that enables real-time communication between multiple users over a network. It consists of a client interface and a server-side component, allowing users to connect via IP address and port and exchange messages seamlessly.

## Features

- **Real-time Communication**: Engage in instant messaging with other users connected to the chatroom.
- **Simple Interface**: The client interface provides an intuitive platform for sending and receiving messages.
- **Multi-User Support**: Multiple users can connect concurrently, fostering group conversations.
- **Basic Security**: Although primarily designed for simplicity and ease of use, the chatroom incorporates basic socket-level security.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/N3MESIScrawl/pvt-chatroom.git
    ```

2. Navigate to the project directory:

    ```bash
    cd zwn-crawl-chatroom
    ```

3. Ensure you have Python installed on your system.

## Usage

To utilize the ZWN CRAWL Chatroom, follow these steps:

1. Start the server:
   
   - Open a terminal window.
  

   - Run the server script:

        ```bash
        python mclientserver.py
        ```

2. Connect to the chatroom:
   
   - Open another terminal window.


   - Run the client script:

        ```bash
        python clientinterface.py
        ```

3. Enter the server IP address and port number as prompted.
4. Choose a username and start sending messages.

## Exiting

- To exit the client interface, press `Ctrl + C`.
- To stop the server, press `Ctrl + C` in the terminal where the server is running.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request


This project is licensed under the MIT License.

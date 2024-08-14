import socket

HOST = '127.0.0.1'  # Use the server's IP address or 'localhost' if running on the same machine
PORT = 12345  # Use the same port number as the server

def send_message(msg):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(msg.encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print("Bot: " + response)
    client.close()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        send_message(user_input)

import socket

PC_B_IP = "192.168.1.50"  # replace with PC B's actual IP
PORT = 9999

message = input("Enter message to send: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((PC_B_IP, PORT))
s.send(message.encode())
s.close()
print("Message sent.")

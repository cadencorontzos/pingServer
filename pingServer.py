# UDP Ping Server
# Using random to simulate packet loss
import random
# Import socket module
from socket import *

# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print('Server Active...')
while True:

    # Receive client packet and arrival address
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message
    message = message.upper()

    #Simulates a 20% packet loss rate
    if(random.randint(1,10) >2):
        # If no packet loss, server responds
        serverSocket.sendto(message, address)


# UDP Ping Client
from socket import *
from time import time

clientSocket = socket(AF_INET, SOCK_DGRAM)

#Gets the server name and port number
print('This ping program will send 10 pings the given IP and give the RTT, as well as the average RTT.')
serverName = input('What is the IP of the server you would like to ping? > ')
serverPort = int(input('On what port? > '))

#Gives the system time in ms
milliseconds = lambda: int(time() * 1000)

#Variables for the ping stats
packetsRecieved = 0
totalDelay = 0

#Set the timeout
clientSocket.settimeout(1)

for i in range(1,11):
    try:
        now = milliseconds()
        #Send ping
        clientSocket.sendto('ping'.encode(), (serverName,serverPort))

        #Recieve response
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

        
        #Calculates the delay and packets recieved
        delay = milliseconds()-now
        totalDelay +=delay
        packetsRecieved +=1

        #Print response
        print(str(i) + ". " + modifiedMessage.decode() + ' ' +str(delay) + ' ms')

    except:
        #Print *                                                                      
        print(str(i) + '. *')
        
#Prints the av delay and packet loss rate
if packetsRecieved > 0:
    print('The average delay was ' + str(totalDelay/packetsRecieved) + ' ms.')
else:
    print('No packets made it back :( yikes.')
print('The packet loss rate was ' + str(packetsRecieved/10) + '.')

#Closes client socket
clientSocket.close()




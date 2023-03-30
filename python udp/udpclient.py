import socket #import pythons socket library

serverName='hostname'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #create udp socket fro server
message= input('input lowercase sentence') #get user keyboard input
clientSocket.sendto(message,(serverName,serverPort)) #attach server name, port to message, send into socket
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # read reply character from socket into string
print(modifiedMessage) #print out received string and close socket
clientSocket.close()

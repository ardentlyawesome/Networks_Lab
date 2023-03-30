## My Repository of Socket Programming Programs I did as a part of my Computer Networks Course in College

Socket Programming an Intro: 

Goal: learn how to build client/server applications that communicate using sockets

Socket: Dropbox between application process and end-end transport protocol

Two socket types for two transport services: 
1. UDP: Unreliable Datagram 
2. TCP: Reliable, byte stream-oriented

Socket Programming with UDP:
- no handshaking before sendin Data
- sender explicitly attaches IP destination address and port # to each packet
- rcvr extracts sender IP address and port # from recieved packet

UDP: transmitted data may be lost or recieved out of order

Application Viewpoint: provides unreliable transfer of groups of bytes ("datagrams") between client and server.

Socket Programming with TCP 
- client must contact server:
1. server must be first running
2. server must have created socket (dropbox) that welcomes client's contact

-server accepts connect by:
1. creating new connection specific socket
2. allows server to talk with multiple clients

-client connects to server by:
1. creating TCP socket, specifying IP Address, port number of server process
2. client socket is now bound to that specific server
<br>

---







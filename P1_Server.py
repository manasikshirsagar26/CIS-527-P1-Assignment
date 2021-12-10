#!/usr/bin/env python3
#######################################################
# CIS 527: Computer Networks
# Name: Manasi Kshirsagar
# UMID- 05494807
# Instructor: Prof. Zheng Song
# Semester: Fall 2021 
# P1 assignment: Socket Programming - Server Side
#######################################################


import socket

#############################################################################
################     Disclaimer ################
###### Following section of code finds IP address automatically 
#       when this file runs on any computer(connected to internet)
#       However, port 80 might be busy, in that case, 
#       this file when run will produce errors on terminal.
#       In that casem Kindly comment following section and hardcode appropriate server IP below. 
# Find server IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("Server IP: ", s.getsockname()[0]) # Server IP address
SERVER_IP = s.getsockname()[0]
s.close()
################    End of Disclaimer   ################
#############################################################################

# Configure Server IP below
# SERVER_IP = '192.168.0.11'

# Define server port using UMID
SERVER_PORT = 4807
acknowledgment = '200 OK'       # Intializing the ACK signal value
message_of_the_day = 'Anyone who has never made a mistake has never tried anything new.'  # Initializing Message of the day value                                     
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))                                # Associate the socket with a specific network interface and port number
    s.listen()                                                      # listens for connections from client
    conn, addr = s.accept()                                         # to establish a connection to the server and initiate the three-way handshake
    with conn:
        while True:
            receivedData = conn.recv(1024)                          
            receivedData = receivedData.decode()
            print(receivedData)
            if not receivedData:
                print('No data received from client. Exiting program.\n')
                break
            elif (receivedData == 'MSGGET\n'):
                sending = acknowledgment +'\n   '+ message_of_the_day + '\n'
                conn.sendall(sending.encode())
            elif (receivedData == 'MSGSTORE\n'):
                #print('This is msg store\n',receivedData)
                conn.sendall(acknowledgment.encode())
                receivedData = conn.recv(1024)
                receivedData = receivedData.decode()
                message_of_the_day = receivedData
                conn.sendall((acknowledgment+'\n').encode())

            

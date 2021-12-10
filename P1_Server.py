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

CLIENT = '127.0.0.1'  # Standard loopback interface address (localhost)
SERVER_PORT = 4807        # Port to listen on (non-privileged ports are > 1023)
acknowledgment = '200 OK'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((CLIENT, SERVER_PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        # print('Connected by', addr)
        message_of_the_day = 'Anyone who has never made a mistake has never tried anything new.'
        while True:
            receivedData = conn.recv(1024)
            receivedData = receivedData.decode()
            if not receivedData:
                break
            elif (receivedData == 'MSGGET'):
                sending = acknowledgment +'\n'+ message_of_the_day + '\n'
                conn.sendall(sending.encode())
            elif (receivedData == 'MSGSTORE'):
                #print('This is msg store\n')
                conn.sendall(acknowledgment.encode())
                receivedData = conn.recv(1024)
                receivedData = receivedData.decode()
                message_of_the_day = receivedData
                # print('Updated : message_of_the_day: ' + message_of_the_day)
                conn.sendall(acknowledgment.encode())
            #print(data)
            #print(type(data))
            

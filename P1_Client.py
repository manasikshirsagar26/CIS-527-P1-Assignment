#!/usr/bin/env python3
#######################################################
# CIS 527: Computer Networks
# Name: Manasi Kshirsagar
# UMID- 05494807
# Instructor: Prof. Zheng Song
# Semester: Fall 2021 
# P1 assignment: Socket Programming - Client Side
#######################################################

import socket
import sys

SERVER_IP = sys.argv[1] #'127.0.0.1'  # The server's hostname or IP address
print("server ip provided", SERVER_IP)
SERVER_PORT = 14807        # Server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP,SERVER_PORT))
    while(True):
        print('\n')
        client_input = input('Please provide input MSGGET or MSGSTORE or EXIT: ')
        if (client_input == 'MSGGET'):
            print('c: MSGGET')
            s.sendall(client_input.encode())
            receivedData = s.recv(1024)
            receivedData = receivedData.decode()
            print('s: '+receivedData)
            # print(str(repr('s:'+receivedData)))
        elif (client_input == 'MSGSTORE'):
            print('c: MSGSTORE')
            s.sendall(client_input.encode())
            # print('Client request msg store')
            receivedData = s.recv(1024)
            receivedData = receivedData.decode()
            # print('Data is :'+ receivedData)
            # print('ack received from server')
            if (receivedData == '200 OK'):
                # print(repr(receivedData))
                print('s: '+receivedData)
                message_of_the_day = 'Imagination is more important than knowledge.'
                print('c: '+ message_of_the_day)
                s.sendall(message_of_the_day.encode())
                receivedData = s.recv(1024)
                receivedData = receivedData.decode()
                print('s: '+receivedData)
                # print(repr(receivedData))
        elif (client_input == 'EXIT'):
            print('Exit requested by user. Exiting the program.')
            break
        else:
            print('Unrecognised Input, Please provide input MSGGET or MSGSTORE')
            break
        


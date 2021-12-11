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
SERVER_PORT = 4807        # Server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP,SERVER_PORT))  # Connection established between client and server
    while(True):
        print('\n')
        client_input = input('Please provide input MSGGET or MSGSTORE or EXIT: ')
        if (client_input == 'MSGGET'):           ## MSGGET Command
            client_input = client_input +'\n'
            print('c: MSGGET')
            s.sendall(client_input.encode())     # Send the encoded data over the network from client to server
            receivedData = s.recv(1024)          # Receieved the encoded data from Server
            receivedData = receivedData.decode() # Decode the received data received from server
            print('s: '+ receivedData)           # print the received decoded data
        elif (client_input == 'MSGSTORE'):       ## MSGSTORE Command
            client_input = client_input +'\n'
            print(client_input)                 
            print('c: MSGSTORE')
            s.sendall(client_input.encode())    # Send the encoded data over the network from client to server
            receivedData = s.recv(1024)         # Receieved the encoded data from Server
            receivedData = receivedData.decode()# Decode the received data received from server
            #print("received:",receivedData)
            if (receivedData == '200 OK'):      # If Received data is ACK i.e '200 OK' , proceed if further steps
                print('s: '+receivedData)
                message_of_the_day = 'Imagination is more important than knowledge.' # default update value for message of the day
                print('Default input message of the day is: ', message_of_the_day)
                user_input_message_of_the_day = input('Please provide message of the day: ') # User input for message of the day
                if (user_input_message_of_the_day != ''):
                    message_of_the_day = user_input_message_of_the_day
                print('c: '+ message_of_the_day)
                s.sendall(message_of_the_day.encode())      # Encode the message of the day value and send it from client to server
                receivedData = s.recv(1024)                 # Receive the ACK message
                receivedData = receivedData.decode()        # Decode the received ACK message
                print('s: '+receivedData)                   # Print the ACK message
            else:
                print('ACK not received. Please resend the data')
                continue
        elif (client_input == 'EXIT' or client_input == 'exit' or client_input =='Exit'):  # Exit the program
            print('Exit requested by user. Exiting the program.')
            break
        else:
            print('Unrecognised Input, Please try again') # Unrecognised input 
            continue



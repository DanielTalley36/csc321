#
#   Weather update client
#   Connects SUB socket to tcp://localhost:5556
#   Collects weather updates and finds avg temp in zipcode
#

import sys
import zmq


#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.REP)

socket.bind("tcp://*:5556")

while True:
    msg = socket.recv_string()
    print('From client : ',msg)
    smsg = input('enter your message here : ')
    socket.send_string(smsg)
    print()




import sys
import zmq


#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://node00:5556")

while True:
    msg = input ('enter your msg here : ')
    socket.send_string(msg)
    print ('sending', msg)
    print ('From sever : ', socket.recv_string())
    print()
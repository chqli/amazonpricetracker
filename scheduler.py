import time

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:7000")
datacsv = "C:\\Users\\pranami\\Downloads\\data.csv"
while True:
    socket.send_string('tick')
    print('tick')
    time.sleep(5)

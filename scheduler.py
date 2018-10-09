import os
import time

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
if os.name == 'nt':
    socket.bind("tcp://127.0.0.1:7000")
else:
    socket.bind("ipc:///tmp/scheduler")
datacsv = "C:\\Users\\pranami\\Downloads\\data.csv"
while True:
    socket.send_string('tick')
    print('tick')
    time.sleep(5)

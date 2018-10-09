import os
import time

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
if os.name == 'nt':
    socket.connect("tcp://127.0.0.1:5000")
else:
    socket.connect("ipc:///tmp/datamanager")
while True:
    socket.send_string('asdf')
    msg = socket.recv_pyobj()
    print(msg)
    time.sleep(2)

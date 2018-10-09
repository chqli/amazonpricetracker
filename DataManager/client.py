import time

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
# socket.bind("ipc:///tmp/datamanager")
socket.connect("tcp://127.0.0.1:5000")
while True:
    socket.send_string('asdf')
    msg = socket.recv_pyobj()
    print(msg)
    time.sleep(2)

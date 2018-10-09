import os

import zmq

from DataManager.data_manager import BatchReadLines

context = zmq.Context()
socket = context.socket(zmq.REP)
if os.name == 'nt':
    socket.bind("tcp://127.0.0.1:6000")
else:
    socket.bind("ipc:///tmp/datamanager")
datacsv = "C:\\Users\\pranami\\Downloads\\data.csv"
manager = BatchReadLines(datacsv, 5)
while True:
    msg = socket.recv()
    batch = manager.get_batch()
    elem = next(batch)
    socket.send_pyobj(elem)

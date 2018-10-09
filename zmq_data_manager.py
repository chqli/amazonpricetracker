import zmq

from data_manager import BatchReadLines

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:6000")
datacsv = "data.csv"
manager = BatchReadLines(datacsv, 5)
while True:
    msg = socket.recv()
    batch = manager.get_batch()
    elem = next(batch)
    socket.send_pyobj(elem)

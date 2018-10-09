import zmq

from DataManager.data_manager import BatchReadLines

context = zmq.Context()
socket = context.socket(zmq.REP)
# rc = socket.bind("ipc:///tmp/datamanager")
rc = socket.bind("tcp://127.0.0.1:5000")
datacsv = "C:\\Users\\pranami\\Downloads\\data.csv"
manager = BatchReadLines(datacsv, 5)
while True:
    msg = socket.recv()
    batch = manager.get_batch()
    elem = next(batch)
    socket.send_pyobj(elem)

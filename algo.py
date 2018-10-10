import asyncio
import csv
import json
import time
from io import StringIO

import aiohttp
import zmq


class Record:

    def __init__(self, ts, amount) -> None:
        super().__init__()
        self.ts = ts
        self.amount = amount


def parse_record_csv(record):
    f = StringIO(record)
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        return Record(int(row[0]), float(row[1]))


def get_price_average(records):
    if not len(records):
        return 0.0
    total = sum(map(lambda x: x.amount, records))
    return total / len(records)


async def get_sold_status():
    _id = await post_register_request()
    time.sleep(3)
    return await poll_request_data(_id)


async def post_register_request():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:5000/register-request", timeout=3) as resp:
            read = await resp.read()
            json_data = json.loads(read)
            return json_data['id']


async def poll_request_data(_id):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:5000/request-data/{}".format(_id), timeout=3) as resp:
            read = await resp.read()
            json_data = json.loads(read)
            return json_data['sold']


def get_recent_average():
    socket.send_string('asdf')
    msg = socket.recv_pyobj()
    records = [parse_record_csv(x) for x in msg]
    print("For timestamps {} to {}".format(records[0].ts, records[-1].ts))
    return get_price_average(records)


context = zmq.Context()
socket = context.socket(zmq.REQ)
scheduler_socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:6000")

scheduler_socket.connect("tcp://127.0.0.1:7000")
scheduler_socket.setsockopt_string(zmq.SUBSCRIBE, '')
loop = asyncio.get_event_loop()


def next_price(avg_price, was_sold):
    if was_sold:
        return avg_price * 1.1
    return avg_price * 0.9


async def run():
    while True:
        scheduler_socket.recv_string()
        next_avg = loop.run_in_executor(None, get_recent_average)
        was_sold_task = loop.create_task(get_sold_status())
        tasks = await asyncio.gather(was_sold_task, next_avg)
        print("Price to be set is {}".format(round(next_price(tasks[1], tasks[0]), 2)))


try:
    loop.run_until_complete(asyncio.gather(run()))
finally:
    loop.close()

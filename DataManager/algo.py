import asyncio
import csv
import json
import logging
import os
from io import StringIO

import aiohttp
import zmq
from dataclasses import dataclass


@dataclass
class Record:
    ts: int
    amount: float


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


async def do_post_poll():
    _id = await post_request_to_api_server()
    return await poll_request_to_api_server(_id)


async def post_request_to_api_server():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:5000/register-request", timeout=3) as resp:
            read = await resp.read()
            json_data = json.loads(read)
            return json_data['id']


async def poll_request_to_api_server(id):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:5000/request-data/{}".format(id), timeout=3) as resp:
            read = await resp.read()
            json_data = json.loads(read)
            return json_data['sold']


def get_next_average():
    socket.send_string('asdf')
    msg = socket.recv_pyobj()
    records = [parse_record_csv(x) for x in msg]
    return get_price_average(records)


context = zmq.Context()
socket = context.socket(zmq.REQ)
if os.name == 'nt':
    socket.connect("tcp://127.0.0.1:6000")
else:
    socket.connect("ipc:///tmp/datamanager")
loop = asyncio.get_event_loop()

logging.basicConfig(level=logging.DEBUG)


def next_price(avg_price, was_sold):
    if was_sold:
        return avg_price * 1.1
    return avg_price * 0.9


async def try_these():
    while True:
        next_avg = loop.run_in_executor(None, get_next_average)
        flag_task = loop.create_task(do_post_poll())
        gather = await asyncio.gather(flag_task, next_avg)
        print(next_price(gather[1], gather[0]))


try:
    loop.run_until_complete(asyncio.gather(try_these()))
finally:
    loop.close()

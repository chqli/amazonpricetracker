import time
import csv
from io import StringIO

from dataclasses import dataclass


@dataclass
class Record:
    ts: int
    amount: float


class BatchReadLines:
    def __init__(self, file_source, batch_size) -> None:
        self.BUFFER_SIZE = 100
        super().__init__()
        self.file_source = file_source
        self.batch_size = batch_size
        self.file_gen = self.read_to_buffer()
        # Discard the header
        [x for x in self.get_batch(1)]

    def get_batch(self, batch_len=None):
        if batch_len is not None:
            bsize = batch_len
        else:
            bsize = self.batch_size
        lst = [x for _, x in zip(range(bsize), self.file_gen)]
        yield lst

    @staticmethod
    def parse_record_csv(record):
        f = StringIO(record)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            return Record(row[0], row[1])

    def read_to_buffer(self):
        with open(self.file_source) as fh:
            while True:
                lines = fh.readlines(self.BUFFER_SIZE)
                if len(lines) is 0:
                    break
                yield from lines


def read_every_tick(seconds, manager):
    while True:
        time.sleep(seconds)
        gen = manager.get_batch()
        print(next(gen))
        print("one tick")

# datacsv = "C:\\Users\\pranami\\Downloads\\data.csv"
# manager = BatchReadLines(datacsv, 5)
# read_every_tick(2, manager)

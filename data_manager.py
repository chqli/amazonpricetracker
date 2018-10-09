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

    def read_to_buffer(self):
        with open(self.file_source) as fh:
            while True:
                lines = fh.readlines(self.BUFFER_SIZE)
                if len(lines) is 0:
                    break
                yield from lines

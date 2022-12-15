"""
Python Script to generate logs for testing purposes
"""
import logging
import time
import random
import string
from logging import StreamHandler

"""
Custom Designed File Handler to close the file handler after every log entry
closing the file handler after every log entry will close the log file and let filebeat read the file
Handler reopens the file and writes the new log entry  and closes it back again to allow filebeat to read the new log line e

"""
class QuickReleaseFileHandler(StreamHandler):
    def __init__(self, filename_getter):
        super().__init__()
        self.stream = None
        self.filename_getter = filename_getter

    def setStream(self, stream):
        raise NotImplementedError("You can't call setStream on this handler")

    def flush(self) -> None:
        pass  # we don't need to flush, since we close the stream after every message

    def emit(self, record) -> None:
        with open(self.filename_getter(record), 'a') as self.stream:
            super().emit(record)
        self.stream = None


fh = QuickReleaseFileHandler(
    lambda _: 'file.log',
)

logging.basicConfig(level=logging.INFO, handlers=[fh])
logNumber = 1

while True:
    logging.info(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150)))
    logging.error(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150)))
    print("Log Number: " + str(logNumber))
    logNumber = logNumber + 1
    time.sleep(10)

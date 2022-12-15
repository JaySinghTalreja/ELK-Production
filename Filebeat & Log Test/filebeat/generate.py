#import all packakges generate logs to file.log every 1 sec of type INFO and ERROR with random messages of length 150
# import random
# import logging
# import time
# import string

# #Log to file and close the handler
# def logToFileAndCloseHandler():
#     logger = logging.getLogger()
#     #logger.setLevel(logging.INFO)
#     logNumber = 0
#     while True:
#         fileHandler = logging.FileHandler('file.log')
#         # fileHandler.setLevel(logging.INFO)
#         logger.addHandler(fileHandler)
#         logger.info(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150)))
#         logger.error(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150)))
#         print("Log Number: " + str(logNumber))
#         logNumber = logNumber + 1
#         fileHandler.close()
#         time.sleep(1)


# logging.basicConfig(filename='file.log', level=logging.INFO)
# logging.basicConfig(filename='file.log', level=logging.ERROR)
# logNumber = 0
# while True:
#     logging.info(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150)))
#     logging.error(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150)))
#     print("Log Number: " + str(logNumber))
#     logNumber = logNumber + 1
#     time.sleep(1)



import logging
import time
from logging import StreamHandler


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

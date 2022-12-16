import logging
import time
import random
import string
from logging import StreamHandler

"""
Custom Designed File Handler to close the file handler after every log entry
closing the file handler after every log entry will close the log file and let filebeat read the file
Handler reopens the file and writes the new log entry  and closes it back again to allow filebeat to read the new log line
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

#Generate JSON Logs with data timestamp, messeage, app and error message using python script
def generateJSONLogs():
    import json
    import time
    import random
    import string
    import datetime
    logging.basicConfig(level=logging.INFO, handlers=[fh]) #set this handle for every log level, ex CRITICAL, ERROR, WARNING, INFO, DEBUG
    logNumber = 1
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = ''.join("Random Message" + str(logNumber))
        requestData = {
            "id": ''.join(random.choice(string.digits) for _ in range(10)),
            "name": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            "email": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + '@' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + '.com',
            "phone": ''.join(random.choice(string.digits) for _ in range(10)),
            "address": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            "city": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            "state": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            "zip": ''.join(random.choice(string.digits) for _ in range(10)),
            "country": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            "ip": ''.join(random.choice(string.digits) for _ in range(10)) + '.' + ''.join(random.choice(string.digits) for _ in range(10)) + '.' + ''.join(random.choice(string.digits) for _ in range(10)) + '.' + ''.join(random.choice(string.digits) for _ in range(10)),
            "user_agent": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            "created_at": timestamp,
            "updated_at": timestamp
        }
        app = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        error = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150))
        #define the data to be logged
        data = {
            "timestamp": timestamp,
            "message": message,
            "requestData": requestData,
            "app": app,
            "error": error
        }
        logging.info(json.dumps(data))                                                                                    ") #add spaces to make the log file size bigger
        print("Log Number: " + str(logNumber))
        logNumber = logNumber + 1
        time.sleep(5)

generateJSONLogs()

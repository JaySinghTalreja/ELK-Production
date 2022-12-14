#import all packakges generate logs to file.log every 1 sec of type INFO and ERROR with random messages of length 150
import random
import logging
import time
import string
import os
import sys
import glob
import shutil

logging.basicConfig(filename='file.log', level=logging.INFO)
logging.basicConfig(filename='file.log', level=logging.ERROR)
logNumber = 0
while True:
    logging.info(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150)))
    logging.error(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(150)))
    print("Log Number: " + str(logNumber))
    time.sleep(1)
#!/usr/bin/env python3
'''This is the logger file.
It contains the logger configuration.
'''
import colorlog
import logging
import sqlite3

import utils


# Configure logging variables
LOG_LEVEL = logging.DEBUG
LOGFORMAT = '%(log_color)s%(levelname)-10s%(reset)s[%(asctime)s] %(name)s: %(message)s'
DATEFORMAT = '%d/%b/%Y %H:%M:%S'

# Create a custom formatter to color the levelname
class LevelnameColoredFormatter(logging.Formatter):
    LEVELNAME_COLORS = {
        'DEBUG': '\033[36m',
        'INFO': '\033[32m',
        'WARNING': '\033[33m',
        'ERROR': '\033[31m',
        'CRITICAL': '\033[41m',
    }

    def format(self, record):
        levelname = record.levelname
        color = self.LEVELNAME_COLORS[levelname]
        record.levelname = f'{color}{levelname}\033[0m'
        return super().format(record)

# Define a custom handler to write log messages to the database
class DatabaseHandler(logging.Handler):
    def emit(self, record):
        cursor.execute("INSERT INTO logs VALUES (?, ?, ?, ?)", (record.levelname, utils.currentTime, record.name, record.msg))
        conn.commit()

# Connect SQLite database
db_file = 'resources/dev_database.sqlite'
conn = sqlite3.connect(db_file, check_same_thread=False)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""CREATE TABLE IF NOT EXISTS logs (level text, time text, service text, message text)""")
conn.commit()
    
# Set up the logger
log = logging.getLogger() # 'pythonConfig'

#Set logging level
log.setLevel(LOG_LEVEL)

# Create a handler for writing to the console and database
stream = colorlog.StreamHandler()
stream = DatabaseHandler()

# Set formatter
formatter = colorlog.ColoredFormatter(LOGFORMAT, datefmt=DATEFORMAT,
    log_colors={
        'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
            'SUCCESS': 'green'
    })
stream.setFormatter(formatter)

# Add handler to the logger
log.addHandler(stream)
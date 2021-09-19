'''
References:
    https://docs.python.org/3/library/syslog.html
    https://www.loggly.com/use-cases/python-syslog-how-to-set-up-and-troubleshoot/


On Ubuntu you can use the log tool to view and search for all log messages.
Alternatively, you can use dmesg.
'''

###############################################################################
# Import Libraries
###############################################################################
import os
import sys
from decouple import config

import logging
import logging.handlers
from logging.handlers import SysLogHandler


###############################################################################
# Define Directories
###############################################################################
dir_base = config('dir_root')
dir_scripts = os.path.join(dir_base, 'scripts')
dir_results = os.path.join(dir_base, 'results')
[sys.path.append(d) for d in [dir_base, dir_scripts]]


###############################################################################
# Functions
###############################################################################
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(facility=SysLogHandler.LOG_DAEMON,
                                         address = '/dev/log')
logger.addHandler(handler)

logger.debug('Your log message')

















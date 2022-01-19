'''
Description:
    - Test papertrail logging service

References:
    - https://docs.python.org/3.5/library/logging.html
    - https://docs.python.org/3/howto/logging-cookbook.html
    - https://www.papertrail.com/blog/papertrail-for-python-logs/
    - https://www.papertrail.com/help/configuring-centralized-logging-from-python-apps/

Debugging Log Issues:
    - https://www.papertrail.com/help/troubleshooting-remote-syslog-reachability/#basic-ip-reachability

'''

###############################################################################
# Import Libraries
###############################################################################
import os
import sys
import logging
import socket
from logging.handlers import SysLogHandler
#from decouple import config

# Add Filter
class ContextFilter(logging.Filter):
    hostname = socket.gethostname()
    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True

# Get Formatter 
format = '%(asctime)s | %(hostname)s | %(message)s'
formatter = logging.Formatter(format, datefmt='%b %d %H:%M:%S')

# Get Syslogger 
syslog = SysLogHandler(address=('logs2.papertrailapp.com', 53749))
syslog.setLevel(logging.DEBUG)
syslog.setFormatter(formatter)
syslog.addFilter(ContextFilter())

# Get Handler (To-IO)
io = logging.StreamHandler()
io.setLevel(logging.DEBUG)
io.setFormatter(formatter)


# Get Logger & Add Handlers 
logger = logging.getLogger(name = 'test-core-commercial')
logger.addHandler(syslog)
logger.addHandler(io)
logger.setLevel(level = logging.DEBUG)


logger.warning('smoke-test-core-commercial')


"""

# Get Logger
logger = logging.getLogger(name='my_logger')

# Create Formater(s)
'''Note: subjects & values are additional parameters that must be passed as key/value
    pairs when logging'''
formatter = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(hostname)s | %(source)s | %(f_name)s | %(message)s | %(subject)s | %(values)s')

# Get Handlers (To-File)
fh = logging.FileHandler('errors.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)


# Get Handler (To-IO)
io = logging.StreamHandler()
io.setLevel(logging.INFO)
io.setFormatter(formatter)

# Add Handlers
logger.addHandler(fh)
logger.addHandler(io)


# My Logger Function 
def my_logger(
    level: str,
    message: str,
    source : str = None,
    f_name: str = None,
    subject: str = None,
    values: str = None):
    '''
    Generic function to log message and additional fields.
    source: program name giving rise to logs.  Ex: underwriting prod 1
    f_name: function name giving rise to extra values.
    subject: subject of values.
    values: values to log.  Example: input values
    '''
    hostname = socket.gethostname()
    params = {'hostname': hostname, 'source': source, 'f_name': f_name,
        'subject': subject, 'values': f'{values}'}

    if level.upper() == 'DEBUG':
        logger.debug(message, extra = params)
    elif level.upper() == 'INFO':
        logger.info(message, extra = params)
    elif level.upper() == 'WARNING':
        logger.warning(message, extra = params)
    elif level.upper() == 'ERROR':
        logger.error(message, extra = params)


my_logger(
    level = 'warning',
    message = 'test',
    source = 'my butt',
    f_name = 'my_logger',
    subject = 'i dont know',
    values = '123')

"""








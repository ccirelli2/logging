import logging



logging.basicConfig(
        filename = 'log_output.log', 
        level    = logging.WARNING, 
        format   = '%(asctime)s:%(filename)s:%(process)d:%(levelname)s:%(message)s')


# Example of a user defined log for warning
'''logging.warning('This will be logged to a file')'''

def hello_world():
    print('hello world')


# Example of adding the trace back output to our log error message
'''
try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    logging.error('Failed to open file', exc_info=True)
'''

File = '/home/ccirelli2/Desktop/Programming/Python_logging/log_output.log'


# Example #2:  Note, because no exception is raised the trace back is not added to the log. 
'''
try:
    open(File, 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception:
    logging.error('Failed to open file', exc_info=True)
'''


import sys

try:
        a = 1/0
except Exception:
    exc_tuple = sys.exc_info()
    print(exc_tuple)
    print('\n', type(exc_tuple))









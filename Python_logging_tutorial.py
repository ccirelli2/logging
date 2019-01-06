'''
Reference:      https://mail.google.com/mail/u/0/#inbox/FMfcgxwBTshfNpZQdpvvRFkcQFKNRTTm?projector=1
Pydocs:         https://docs.python.org/3.6/library/logging.html

'''


#LOGGING LEVELS 
'''
DEBUG:      Detailed information typically of interest only when diagnosing problems.
INFO:       Confirmation that things are working as expected
WARNING:    An indication that something has unexpectedly happened or indicative of some problem
            in the near future.  The software is still working as expected
ERROR:      Due to a more serious problem the software has not been able to perform some function
CRITICAL:   A serious error indicating that the program itself may be unable to continue running. 
'''

# IMPORT LOGGING MODULE
import logging

# Set Default 
'''logging.basicConfig(level=logging.DEBUG)'''

# Create a Log File
'''
Output:     route output to a file
Note:       appends to file as opposed to writing over. 
Format:     Allows you to customize the log output (example add time, type of message, etc)
            Syntax:  You need to separate each attribute with a ':' colon
'''
logging.basicConfig(filename = 'test.log', level=logging.DEBUG, 
        format='%(asctime)s:%(levelname)s:%(message)s') 


# DEFINE SIMPLE FUNCTIONS
def addition(x,y):
    return x+y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y


# NUMBER OBJECTS
num_1 = 10
num_2 = 5


# STANDARD OUTPUT-------------------------------
add_result = addition(num_1, num_2)
#print(add_result)
sub_result = subtraction(num_1, num_2)
#print(sub_result)
multi_result = multiplication(num_1, num_2)
#print(multi_result)
divi_result = division(num_1, num_2)
#print(divi_result)




# REPLACE WITH LOGGING STATEMENTS--------------
'''
SETTING:        Default set to ERORR. 
'''

# Set to Default
logging.debug(add_result)
logging.debug(sub_result)
logging.debug(multi_result)
logging.debug(divi_result)


# Set to Warning
'''
logging.warning(add_result)
logging.warning(sub_result)
logging.warning(multi_result)
logging.warning(divi_result)
'''












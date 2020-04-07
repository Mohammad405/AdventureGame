import time
import random

def print_pause(message, sleep_time=2):
    '''Take a string {message} and an integer {sleep_time}
       print {message}, and pass{sleep_tome} to sleep function
    '''
    print(message)
    time.sleep(sleep_time)

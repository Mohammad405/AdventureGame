import time
import random

def print_pause(message, sleep_time=2):
    '''Take a string {message} and an integer {sleep_time}
       print {message}, and pass{sleep_tome} to sleep function
    '''
    print(message)
    time.sleep(sleep_time)


def intro(item, option):
    ''' Take two prams {item} and {option}
        and display intro messades
    '''
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a " + option + " is somewhere around "
                "here, and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")


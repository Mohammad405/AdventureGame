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


def cave(item, option):
    '''Take two prams {item} and {option}
       print out your options and item in the Cave.
    '''
    
    if "sward" in item:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("\nYou walk back to the field.\n")
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nIt turns out to be only a very small cave.")
        print_pause("\nYour eye catches a glint of metal behind a "
                    "rock.")
        print_pause("\nYou have found the magical Sword of Ogoroth!")
        print_pause("\nYou discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("\nYou walk back out to the field.\n")
        item.append("sward")
    field(item, option)

# TASK - 1

# functions defined to print message accordint to the inputs.


def welcome_msg():
    print ('Stop! Who would cross the Bridge of Death')
    print ("Must answer me these questions three, 'ere the other side he see.\n")


def for_king():
    print ('My liege! You may pass!')


def incorrect_seek():
    print ('Only those who seek the Grail may pass.')


def incorrect_color():
    print ('Incorrect! You must now face the Gorge of Eternal Peril.')


def correct():
    print ('You may pass!')


welcome_msg()  # calling of welcome message function

name = input('What is your name? \n')

if name.lower() == 'arthur':  # checking the name if it maches the name of king
    for_king()
else:

          # using else statement if the name doesn't match the king

    seek = input('What is your quest? \n')
    if 'grail' not in seek.lower():  # checking if the word grail is their in input
        incorrect_seek()  # calling function to display if the input doesn't have the word 'grail'
    else:
        color = input('What is your favourite colour? \n')
        if color.lower()[0] == name[0].lower():  # checking the initial of color
            correct()  # calling function if initial matches
        else:
            incorrect_color()  # calling function if initial doesn't matche

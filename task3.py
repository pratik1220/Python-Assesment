# TASK3

import random


def email_check(temp_email):  # function to check the validity of email
    if '@' in temp_email:
        temp_index = temp_email.index('@')
        if temp_email.index('@') >= 2:
            if temp_email[temp_index + 1:] == 'pop.ac.uk':
                return True
    return False


def name_extractor(email):  # function to split name from email and return it
    temp_index = email.index('@')
    name = email[:temp_index]
    name = name.title()
    return name


def chat(email):  # function to continue the chat if email is valid
    operators = ['Janice','Fiona','Arthur','James','Emily','Jack','Will','Ricky'] # for the names of operators to be chose from
    ping = [True,True,True,True,True,True,True,True,True,False]  # for the probability of network error i.e 10%
    extra_choices = ['Hmmm', 'Oh yes', 'I see', 'Tell me more', 'Sorry']  # for the input that donot have specific replies
    name = name_extractor(email)  # calling function and assigning returned name in new variable
    ran_ping = True
    op_name = random.choice(operators) # function to choose randome name of operator from the list 'opereators'

    print (f'Hi, {name}! Thank you, and Welcome to PopChat! My name is {op_name} and it will be my pleasure to help you.')  # string formatting

    while ran_ping == True:  # initializing while loop with ran_ping boolean
        ran_ping = random.choice(ping)  # randomizing the next loop according to the probability
        text_line = input('---> ')

        # Checking certain words in the inputs to determine what to reply

        if 'library' in text_line.lower():
            print ('The library is closed today.')
        elif 'wifi' in text_line.lower():
            print ('WiFi is excellent across the campus.')
        elif 'deadline' in text_line.lower():
            print ('Your deadline has been extended by two working days.')
        elif 'cafeteria' in text_line.lower():
            print ('The opening hours of cafeteria is (8 AM - 8 PM.)')
        elif 'admission' in text_line.lower():
            print ('You can visit college website for its details.')
        elif 'teachers' in text_line.lower():
            print ('The teachers are very friendly and helpful.')
        elif 'sports' in text_line.lower():
            print ('You can play any sports at the ground accordint to your choice.')
        elif text_line.lower() == 'bye' or text_line.lower() == 'exit':
            break  # breaking loop if the input contains bye or exit in it
        else:
            # printing the random replies for not specified word choices
            print (random.choice(extra_choices))
    else:
        print ('*** NETWORK ERROR ***') #Printing network error if the ran_ping is false
    print (f'Thanks,{name}, for using PopChat. See you again soon!')


print ('\nWelcome to Pop Chat One of our operators will be pleased to help you today.')
email = input('Please enter your Poppleton email address: ')

# checking the validity of email by passing entered email in email_check function
if email_check(email) == True:
    chat(email)
else:
    print ('Email should be valid and not be blank!') # printing if the email isn't valid

       

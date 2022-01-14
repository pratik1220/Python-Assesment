# TASK-2


def welcome():  # function for welcome msg
    print ('Swallow Speed Analysis: Version 1.0 \n')


def no_readings():  # function to display msg if there's no input
    print ('No readings entered. Nothing to do.')


def mile_to_km(m):  # function to convert mile into km
    km = m * 1.60934
    return km


def km_to_mile(km):  # function to convert km into mile
    m = km / 1.60934
    return m


def max_speed(array):  # function to return the maximum speed within the list
    array.sort()
    return array[-1]


def min_speed(array):  # function to return the minimum speed within the list
    array.sort()
    return array[0]


def avg_speed(array, count):  # function to calculate the average speed from the list and return it
    total = 0
    for i in array:
        total = total + i
    avg = total / count
    return avg


welcome()
flag = True  # initializing bool as true
total_dis = []
count = 0
while flag:
    read = input('Enter the Next Reading: \n')
    if read == '':
        flag = False  # changing bool value to False if the input is none
        break

    total_dis.append(read)  # inserting the inputs into the list
    count += 1
total_km = []
total_miles = []
if len(total_dis) == 0:  # if statement for checking if list is empty
    no_readings()
    exit

for i in total_dis:  # looping through the list of inputs
    if i[0].upper() == 'U' and i[1:].isnumeric() == True:  # checking if the input in miles is valid
        total_miles.append(float(i[1:]))  # appending only numeric values of miles to new list
    elif i[0].upper() == 'E' and i[1:].isnumeric() == True:

                                                            # checking if the input in kilometers is valid

        total_km.append(float(i[1:]))  # appending only numeric values of kilometers to new list
    else:

        print ('Invalid Inputs! Please Try Again!')
        exit()  # exiting loop if the inputs are invalid
print ('Results Summary \n')
print (len(total_dis), 'Readings Analysed \n')

for i in range(len(total_miles)):
    total_miles[i] = mile_to_km(total_miles[i])  # converting each miles to km by passing it to function
total_miles += total_km  # appending the converted kilometers with the original kilometers inputs

maxtemp = max_speed(total_miles)  # passing list to function to return maximum speed and store it in new variable
mintemp = min_speed(total_miles)  # passing list to function to return minimum speed and store it in new variable
avgtemp = avg_speed(total_miles, count)  # passing list to function to return average speed and store it in new variable

# printing the results in proper format

print ('Max Speed: ', '%.2f' % km_to_mile(maxtemp), 'MPH, ', '%.2f'
       % maxtemp, ' KPH.')
print ('Min Speed: ', '%.2f' % km_to_mile(mintemp), 'MPH, ', '%.2f'
       % mintemp, ' KPH.')
print ('Avg Speed: ', '%.2f' % km_to_mile(avgtemp), 'MPH, ', '%.2f'
       % avgtemp, ' KPH.')

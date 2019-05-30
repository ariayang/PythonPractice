#Exercise 12: List ends

import random

#create a random list
def rand_list (start, end, number):
    custom_list = []
    for i in range (int(number)):
        custom_list.append (random.randint(int(start), int(end)))
    return custom_list

start, end, number = input ('Input 3 integers to generate a list: range start, range end, number of element in the list, seprated by ,').split(',')
custom_list = rand_list (start, end, number)
print ('The random created list is', custom_list)


length = len(custom_list)
new_list = []
new_list.append (custom_list[0])
new_list.append (custom_list[length-1])
print ('The list ends are', new_list)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
import random

def rand(start, end, number):
    a=[]
    for i in range(int(number)):
        a.append(random.randint(int(start),int(end)))
    return a

customlist = []
(i,j,k)=input('To create a random list 1, Specify 3 numbers for range start, finish, and number of elements in the list, split by '',''.').split(',')
a = rand(i,j,k)
(i2,j2,k2)=input('To create a random list 2, Specify 3 numbers for range start, finish, and number of elements in the list.').split(',')
b = rand(i2,j2,k2)

for x in a:
    for y in b:
        if x==y:
            customlist.append (x)

customlist = list (dict.fromkeys(customlist))

print('List 1 is', a)
print('List 2 is', b)

customlist.sort()
print('The common element sorted list is', customlist)

    

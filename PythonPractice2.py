number  = int (input ('Type in a integer number: '))
if number % 2 == 0:
    if number % 4 == 0:
        print (str(number) + ' can be divided by 4.')
    else: print (str (number) + ' is an even number.')
else:
    print (str (number) + ' is an odd number.')


num, check = input ('Type in 2 numbers as number and check: a,b: ').split(',')
num = int (num)
check = int (check)
if check % num == 0:
    print ('Check can be divded by num!')
else: print ('Check cannot be divded by num.')

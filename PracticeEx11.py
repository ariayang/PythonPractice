def division(): #From Practice 4, print out a list of dividers.
    divlist = []
    usernumber = int(input('Please input a number higher than 0 : '))
    if usernumber == 1:
        divlist = [1]
        print (usernumber,'is a prime number.')
    elif usernumber == 2:
        divlist = [1,2]
        print (usernumber,'is a prime number.')
    elif usernumber == 0:
        print('Wrong number.')
    else:
        for elem in range (1,usernumber-1):
            if usernumber % elem == 0:
                divlist.append (elem)

    return divlist, usernumber

custlist, number = division()
print (custlist)

if max (custlist) == 1:
    print (number, 'is a prime number.')
else:
    print (number, 'is not a prime number.')
    

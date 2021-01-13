#Fibonacci
#Ask user to input how many number in Fibonnaci sequence he/she wants to generate

def fib (number):
    if number == 1:
        fib_list = [1]
    elif number == 2:
        fib_list = [1, 1]
    else:
        fib_list = [1, 1]
        for i in range (2, number):
            fib_list.append ((fib_list[i-2]+fib_list[i-1]))

    return fib_list

user = int(input('How many fibonacci number of numbers do you want?'))
print (fib(user))


def fib2 (n):
    fib2(0) = 0
    fib2(1) = 1
    fib2(n) = fib2(n-1) + fib2(n-2)
    return fib2(n)

print(fib2(user))

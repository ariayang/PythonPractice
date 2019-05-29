name = input ('Type in your name: ')
age = int (input ('Type in your age: '))
yearsto100 = 100 - age
year = 2019 + yearsto100
print ('Your name is ' + name)
msg = name + ' will turn 100 in ' + str(year)+'.'

repeat = int(input('How many times to repeat the message? '))
print (repeat * (msg + '\n'))



import random
computerNumber = random.randint(1,9)
count = 0
guessed = 0
 
def guessFunc(guess):
 if guess < computerNumber:
    print('Too low.')
 elif guess > computerNumber:
        print('Too high.')
 else:
     print ('You got it.')
     return 1
     
while True:
    a = guessFunc(int(input ('Input an integer number: ')))
    count += 1
    if a == 1:
        break
    again = input ('Do you want to exit? (if so, type ''exit'') ')
    if again == 'exit':
        break

print ('You guessed it right in ', count, 'times.')

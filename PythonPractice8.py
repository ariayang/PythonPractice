#a = input ('Rock, paper, scissors? ')
#b = input ('Rock, paper, scissors? ')

from random import choice

wins = {'Rock':'Scissors', 'Paper':'Rock', 'Scissors':'Paper'}
options = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}


while True:
    p1 =''
    while not p1 in options:
        p1 = input ('Choose (R)ock, (P)aper or (S)cissors: ').upper()
        if not p1 in options:
            p1=''
            continue
    p1 = options [p1]
    p2 = choice(['Rock', 'Paper', 'Scissors'])
    print('{} vs {}'.format(p1, p2))
    if p1 == p2:
        print ('Draw\n')
        continue
    else:
        if wins[p1] == p2:
            winner = 'Human'
        elif wins[p2] == p1:
            winner = 'Computer'
        print('{} wins\n'.format(winner))
    
                

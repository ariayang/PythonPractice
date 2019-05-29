a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
length = len(a)
newlist = []
for i in a:
    if i < 5:
        newlist.append(i)
print (newlist)

        
number = int(input ('input a number and we''ll generate a list smaller than this number: '))
newlist2 = []
for i in a:
    if i < number:
        newlist2.append(i)
print (newlist2)

print (list (filter (lambda x: x<5, a)))

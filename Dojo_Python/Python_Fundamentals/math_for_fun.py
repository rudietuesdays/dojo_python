# Multiples part i
'''
for count in range (0, 100):
    if (count % 2 == 1):
        print (count)
    else:
        continue
'''

# Multiples part ii
'''
for count in range (5, 1000000):
    if (count % 5 == 0):
        print (count)
    else:
        continue
'''

# Sum List
'''
sum = 0
a = [1, 2, 5, 10, 255, 3]
i = 0
while (i < len(a)):
    sum = sum + a[i]
    i = i + 1
print sum
'''

# Average list
a = [1, 2, 5, 10, 255, 3]
i = 0
sum = 0
avg = 0
while (i < len(a)):
    sum = sum + a[i]
    i = i + 1
avg = sum / (len(a))
print avg

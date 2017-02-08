# odd/even
'''
def odd_even(a, b):
    for count in range (a, b):
        if (count % 2 == 0):
            print "Number is",count,". This is an even number."
        else:
            print "Number is",count,". This is an odd number."
print odd_even(1, 2000)
'''

# multiply
def multiply(arr, num):
    i = 0
    while i < len(arr):
        arr[i] = arr[i] * num
        i = i + 1
    return arr
a = [2,4,10,16]
b = multiply(a, 5)
print b

# Hacker challenge
def layered_multiples(arr):
    new_list = []
    for num in arr:
        inner_list = []
        for i in range (0, num):
            inner_list.append(1)
        new_list.append(inner_list)
    return new_list

x = layered_multiples(multiply([2,4,5],3))
print x

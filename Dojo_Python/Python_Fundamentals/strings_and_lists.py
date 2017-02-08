# Find and replace
str = "If monkeys like bananas, then I must be a monkey!"
print str.find("monkey")
print str.find("monkey", str.find("monkey")+1)
print str.replace("monkey", "alligator")

# Min and max
x = [2,54,-2,7,12,98]
print min(x), max(x)

# First and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]
y = [x[0], x[len(x) - 1]]
print y

# New List
arr = [19,2,54,-2,7,12,98,32,10,-3,6]
arrnew = []
arr.sort()
print arr, arrnew
arrnew.append(arr[0])
arrnew.append(arr[1])
print arr, arrnew
arr.remove(-2)
arr.remove(-3)
print arr, arrnew
arr.insert(0, arrnew)
print arr

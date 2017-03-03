def push_front(arr, val):
    arr.append(arr[len(arr)-1])
    print arr
    x = len(arr) - 1
    print x
    for i in range(len(arr)):
        arr[x], arr[x-1] = arr[x-1], arr[x]
        x -= 1
        print i, x, arr
    arr[0] = val
    print arr
    return arr

arr = [1,2,3,4]
val = 5

push_front(arr, val)

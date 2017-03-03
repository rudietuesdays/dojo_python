def selectionSort(arr):
    # create a for loop to start at the first value
    # find the min
    # keep checking through the array for a lower min
    # once you find the min, send it to the top of the list
    # do it all again with the next lowest
    temp = arr[0]

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            # remember arr[i]
            # when i == length of the array, swap


        if arr[i] < temp:
            temp = arr[i]
            index = i
            print 'temp:', temp, 'index:', i
            print arr
        arr[i], arr[index] = arr[index], arr[i]
        print 'arr is now: ', arr


arr = [6,5,3,1,8,7,2,4]

selectionSort(arr)

def bubbleSort(arr):
    for j in range(len(arr) - 1):
        for i in range((len(arr) - 1) - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print arr

# bubbleSort([5,1,7,4,3])

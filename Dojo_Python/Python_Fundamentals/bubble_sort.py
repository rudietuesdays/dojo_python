def bubbleSort(arr):
    # set var to arr[0]
    # print arr[0]
    # if arr[1] < arr[0]
        # swap arr[1], arr[0]
    # else
        # move on
    # loop through this to check all values

    for j in range(len(arr)-1, 0, -1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                print "i was", arr[i+1]
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print "now i am", arr[i+1]
            print "i =", i
            print "j =", j
            print "arr:", arr


arr = [6,5,3,1,8,7,2,4]

bubbleSort(arr)

### Do it in javascript! ###
#
# function bubble(arr){
#
#   var count = 0;
#
#
#   for (var j = arr.length-1; j>=0; j--){
#     for (var i = 1; i <= j; i++){
#       if (arr[i-1]>arr[i]){
#         var temp = arr[i-1];
#         arr[i-1] = arr[i];
#         arr[i] = temp;
#       }
#     }
#     count++
#     console.log(count)
#   }
#   return arr
# }
#
# var arr = [6,5,3,1,8,7,2,4]
#
# console.log(bubble(arr))

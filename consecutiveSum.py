# Finding maximum sum of k cconsecutive elements in an array

# Using Sliding window method
def getMaxSum(arr,k) :
    maxSum = 0
    i=0
    j=0
    sum = 0
    while i<(len(arr)-k+1) :
        if i == 0 :
            j = 0
            while j < k :
                sum += arr[j]
                j += 1
            # print(sum,i)
        else :
            sum = sum - arr[i-1]
            sum = sum + arr[i+k-1]
            if sum > maxSum :
                maxSum = sum
            # print(sum,i)
        i+=1
    print(maxSum)




getMaxSum([1, 4, 2, 10, 2, 3, 1, 0, 10], 3)
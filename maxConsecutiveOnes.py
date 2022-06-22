# Question Source https://leetcode.com/problems/max-consecutive-ones-iii/
# Using Sliding window method
# Time Complexity  O(n)

class maxConsecutive :
    def __init__(self) :
        self.k = None
        self.arr = []
    def addNums(self, arr, k) :
        self.k = k
        self.arr = arr
    def getMaxConsecutive(self) :

        k = self.k
        arr = self.arr
        print(arr)
        counter = 0
        maxone = 0
        j = 0
        i = 0
        zc = 0 # zero counter

        while j <len(arr) :
            if arr[j] == 1 :
                j+=1
                maxone = max(maxone, j-i)
            elif arr[j] == 0 :
                if zc<k :
                    zc+=1
                    j+=1
                    maxone = max(maxone, j-i)
                elif zc >= k :
                    zc = 0
                    i=j
        print(maxone)

m = maxConsecutive()
m.addNums([1,1,1,0,0,0,1,1,1,1,0,1,1], 2)
m.getMaxConsecutive()
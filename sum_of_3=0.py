# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Question Source: https://leetcode.com/problems/3sum/

def sum(list) :
    target = 0
    ret_sum = []

    for i in range(0,len(list)) :
        temp_list = []
        num1 = list[i]
        temp_list.append(i)
        j = i + 1
        k = j + 1
        while j < len(list) and k < len(list):
            if target - (num1 + list[i] + list[k]) == 0 :
                temp_list = [num1, list[i], list[k]]
                ret_sum.append(temp_list)
                j += 1
                k += 1
            else : 
                k +=1
                
    print(ret_sum)

sum([-1,0,1,2,-1,4])
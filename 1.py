'''
Given An Array of integer target,return indices of the two numbers such that they add up to target
(you may not use same element twice)
input number = [2,7,11,15]
target = 9 ,
Explanation :- "there 2+7 = 9 so Output will be index of 2,7" 
Output = [0,1]
'''

nums=[2,7,11,15]
target = 18
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
            print("[",i,",",j,"]-")

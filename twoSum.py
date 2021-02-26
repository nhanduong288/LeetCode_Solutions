#easy-level problem
#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.

# brute force solution (~500ms)
def twoSum(nums, target):
    result = [0,0]
    for i in range(len(nums)):
        for m in range(i+1, len(nums)):
            if nums[i] + nums[m] == target:
                result[0] = i
                result[1] = m
    return result

d = {0:3, 1:3}
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
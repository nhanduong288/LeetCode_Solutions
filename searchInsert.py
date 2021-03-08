# Leetcode easy
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

def searchInsert(nums, target):
    # if target is in the list, return its index
    if target in nums:
        return nums.index(target)
    # if target is larger than all values, it goes to the end of the list
    elif target > max(nums):
        return len(nums)
    else:
        for num in nums:
            if num > target:
                return nums.index(num)

print(searchInsert([1,3,5,6], 2))
# Leetcode easy
# Given a sorted array nums, 
# remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

# this solution takes >3000ms - long
'''def removeDuplicates(l):
    for num in l:
        while l.count(num) > 1:
            l.remove(num)
    return l'''

# this solution takes < 100ms
def removeDuplicates(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)

print(removeDuplicates([1,1,2]))
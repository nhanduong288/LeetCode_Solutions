# Leetcode easy
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory.

def removeElement(nums, val):
    # using filter
    #return list(filter(val.__ne__,nums))

    # iteration
    # 28ms
    i = 0
    while i < len(nums):
        if nums[i] ==  val:
            nums.remove(nums[i])
        else:
            i += 1
    return nums

print(removeElement([3,2,2,3], 3))
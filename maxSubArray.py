# Leetcode easy
# Given an integer array nums, 
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def maxSubArray(nums):
    ans = nums[0]
    subarr_sum = nums[0]
    for i in range(1, len(nums)):
        print('nums[i]: ' + str(nums[i]) + ' --> ' + 'subarr_sum: ' + str(subarr_sum) + ' --> ' + 'ans: ' + str(ans))
        subarr_sum = max(nums[i], nums[i] + subarr_sum)
        ans = max(ans, subarr_sum)

    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

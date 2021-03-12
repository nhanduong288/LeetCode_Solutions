# Leetcode easy

# Given two sorted integer arrays nums1 and nums2, 
# merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively. 
# You may assume that nums1 has a size equal to m + n 
# such that it has enough space to hold additional elements from nums2.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

"""
        Do not return anything, modify nums1 in-place instead.
"""

def merge(nums1, m, nums2, n):
    for num2 in nums2:
        for num1 in nums1:
            if num2 >= num1 and num2 != 0:
                nums1.insert(num2, nums1.index(num1))
            else:
                nums1.append(num2)
    return nums1

print(merge([1,2,3,0,0,0], 6, [2,5,6], 3))

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order. 

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

from typing import List


class Solution:
    
    def __init__(self,nums=[],target=int):
        self.nums = nums
        self.target = target
        
    def twoSum(self, nums, target):
        if not isinstance(nums,List):
            return "nums is not List!"
        else:
            if len(nums) == 0:
                return "Error: nums is Empty List!"

        if not isinstance(target,int):
            return "target is not integer!"

        sum = 0
        now = 0
        for item in nums:
            if (now==0) and (now <=target):
               sum = item 
            else:
                continue   

                




"""
16. 3Sum Closest
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)

        closest_sum=nums[0]+nums[1]+nums[2]

        for i in range(0,n-2):
            left=i+1
            right=n-1

            while left<right:
                cur_sum=nums[i]+nums[left]+nums[right]

                if abs(cur_sum-target)<abs(closest_sum-target):
                    closest_sum=cur_sum

                if cur_sum<target:
                    left+=1
                elif cur_sum>target:
                    right-=1
                else:
                    return cur_sum
        return closest_sum
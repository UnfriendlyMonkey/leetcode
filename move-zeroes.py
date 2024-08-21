# https://leetcode.com/problems/move-zeroes/submissions/989596929/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

    def moveZeroes2(self, nums):
        # not mine
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1

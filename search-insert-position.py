# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for idx, item in enumerate(nums):
                if item > target:
                    return idx
        return len(nums)


sol = Solution()
nums = [1, 3, 5, 6]
val = 7
print(sol.searchInsert(nums, val))

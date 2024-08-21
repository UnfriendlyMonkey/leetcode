# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


sol = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(sol.removeElement(nums, val))
print(nums)

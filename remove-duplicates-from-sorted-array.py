# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for idx in range(len(nums) - 1, 0, -1):
            if (nums[idx] == nums[idx - 1]):
                nums.pop(idx)
        print(nums)
        return len(nums)


c = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(c.removeDuplicates(nums))
print(nums)

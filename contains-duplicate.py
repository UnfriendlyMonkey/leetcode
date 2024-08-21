# https://leetcode.com/problems/contains-duplicate/submissions/980661238/
# https://leetcode.com/problems/contains-duplicate/submissions/980655286/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for item in nums:
            if d.setdefault(item, 0):
                return True
            d[item] = 1
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


sol = Solution()
assert sol.containsDuplicate([1, 2, 3, 1]) is True
assert sol.containsDuplicate([1]) is False
assert sol.containsDuplicate([4, 5, 6, 7, 8, 9, 0]) is False

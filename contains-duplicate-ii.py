# https://leetcode.com/problems/contains-duplicate-ii/submissions/981445285/
# https://leetcode.com/problems/contains-duplicate-ii/submissions/981452783/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}
        for i, num in enumerate(nums):
            indexes.setdefault(num, []).append(i)
            if len(indexes[num]) > 1:
                if indexes[num][-1] - indexes[num][-2] <= k:
                    return True
        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        # better both in speed and memory
        indexes = {}
        for i, num in enumerate(nums):
            if num in indexes:
                if i - indexes[num] <= k:
                    return True
            indexes[num] = i
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # not mine - slyding window
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False


sol = Solution()
assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False

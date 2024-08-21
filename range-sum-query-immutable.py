# https://leetcode.com/problems/range-sum-query-immutable/submissions/996545273/
# https://leetcode.com/problems/range-sum-query-immutable/submissions/996561433/
from typing import List


class NumArray0:
    # better in memory but slow
    def __init__(self, nums: List[int]):
        self._nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self._nums[left:right + 1])


class NumArray:
    def __init__(self, nums: List[int]) -> None:
        self._sums = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums, 1):
            self._sums[idx] = self._sums[idx - 1] + num

    def sumRange(self, left: int, right: int) -> int:
        return self._sums[right + 1] - self._sums[left]


n = NumArray([1, 2, 3, 4, 5])
assert n.sumRange(0, 4) == 15
n2 = NumArray([-2, 0, 3, -5, 2, -1])
assert n2.sumRange(0, 2) == 1
assert n2.sumRange(2, 5) == -1
assert n2.sumRange(0, 5) == -3

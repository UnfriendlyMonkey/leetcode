# https://leetcode.com/problems/summary-ranges/submissions/984011507/
# beats 91 in speed and 75 in memory
# https://leetcode.com/problems/summary-ranges/submissions/984028524/
# bit slower but better in memory
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        min = max = nums[0]
        for i in nums:
            if i - max > 1:
                result.append(str(min) if min == max else f'{min}->{max}')
                min = max = i
            else:
                max = i
        result.append(str(min) if min == max else f'{min}->{max}')
        return result

    def summaryRanges2(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            result.append(
                str(start) if start == nums[i] else f'{start}->{nums[i]}')
            i += 1
        return result


sol = Solution()
print(sol.summaryRanges2([0, 1, 2, 4, 5, 7]))
print(sol.summaryRanges2([]))
assert sol.summaryRanges2([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert sol.summaryRanges2([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
assert sol.summaryRanges2([]) == []

# https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/1004326030/
# beats 66% in speed and 73% in memory
from typing import List
from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        res = []
        for el in nums1:
            d[el] += 1
        for el in nums2:
            if d[el] > 0:
                res.append(el)
                d[el] -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
    print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4]

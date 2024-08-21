# https://leetcode.com/problems/merge-sorted-array/
# UNFINISHED ONE !!!
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = []
        idx1 = idx2 = 0
        while len(list1) + len(list2) > len(result):
            if not idx1 >= len(list1) and (
                    idx2 >= len(list2)
                    or list1[idx1] <= list2[idx2]):
                result.append(list1[idx1])
                idx1 += 1
            else:
                result.append(list2[idx2])
                idx2 += 1
        return result


res = Solution()
print(res.merge([1, 2, 4], [1, 3, 4]))

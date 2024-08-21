# https://leetcode.com/problems/intersection-of-two-arrays/
# https://leetcode.com/problems/intersection-of-two-arrays/submissions/1001816798/
# https://leetcode.com/problems/intersection-of-two-arrays/submissions/1001864380/
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = set()
        for el in nums1:
            if el in nums2:
                inter.add(el)
        return list(inter)

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return [el for el in set1 if el in set2]
        else:
            return [el for el in set2 if el in set1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([4, 9, 4], [9, 4, 9, 8, 4]))

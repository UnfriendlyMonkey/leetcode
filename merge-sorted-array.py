# https://leetcode.com/problems/merge-sorted-array/submissions/949830940/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while j < n:
            if nums1[i] > nums2[j] or i >= (m + j):
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
            i += 1


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        i = -1 - n
        j = -1
        k = -1

        while abs(i) <= len(nums1) and abs(j) <= n:
            print(i, j, k)
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        while abs(j) <= n:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


sol = Solution2()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
sol.merge(nums1, m, nums2, n)
print(nums1)

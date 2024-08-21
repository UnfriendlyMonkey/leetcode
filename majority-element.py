# https://leetcode.com/problems/majority-element
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/majority-element/submissions/968812590/
        counters = {}
        max = len(nums) // 2
        if len(nums) < 3:
            return nums[0]
        for item in nums:
            counter = counters.setdefault(item, 0) + 1
            if counter > max:
                return item
            counters[item] = counter

    def majorityElement_2(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        # https://leetcode.com/problems/majority-element/submissions/969019787/
        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = nums[i]
                    count = 1

        return candidate

    def majorityElement_3(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement_4(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/majority-element/submissions/969027094/
        for item in set(nums):
            if nums.count(item) > len(nums) // 2:
                return item

# https://leetcode.com/problems/third-maximum-number/
# https://leetcode.com/problems/third-maximum-number/submissions/1329643431/


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        max_1 = max_2 = max_3 = None
        # or -inf
        print(max_1, max_2, max_3)
        for i in nums:
            if i in [max_1, max_2, max_3]:
                continue
            if max_1 is None or i > max_1:
                max_1, max_2, max_3 = i, max_1, max_2
            elif max_2 is None or i > max_2:
                max_2, max_3 = i, max_2
            elif max_3 is None or i > max_3:
                max_3 = i
        print(max_1, max_2, max_3)
        if max_2 == max_3 or max_3 is None:
            return max_1
        return max_3


sol = Solution()
assert sol.thirdMax([1, 2, 4]) == 1
assert sol.thirdMax([2, 2, 3, 1]) == 1
assert sol.thirdMax([1, 2, -23434353]) == -23434353

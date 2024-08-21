# https://leetcode.com/problems/sqrtx/


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, root = 0, x, -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                root = mid
                left = mid + 1
            else:
                right = mid - 1
        return root


s = Solution()
print(s.mySqrt(10001))

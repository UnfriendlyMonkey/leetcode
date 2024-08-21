# https://leetcode.com/problems/climbing-stairs/
# Didn't pass - Time limit excedeed


class Solution:
    def climbStairs(self, n: int) -> int:

        def _count_variants(branch: list) -> None:
            s = sum(branch)
            if s == n:
                variants.append(branch)
                return
            if s > n:
                return
            _count_variants(branch[:] + [1])
            _count_variants(branch[:] + [2])

        variants = []
        _count_variants([1])
        _count_variants([2])

        print(variants)
        return len(variants)


s = Solution()
n = 7
print(s.climbStairs(n))

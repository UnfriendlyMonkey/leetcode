# https://leetcode.com/problems/valid-perfect-square/
# https://leetcode.com/problems/valid-perfect-square/submissions/1031410301/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while True:
            ii = i * i
            if ii == num:
                return True
            if ii > num:
                return False
            i += 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPerfectSquare(3))
    print(sol.isPerfectSquare(4))
    print(sol.isPerfectSquare(113))
    print(sol.isPerfectSquare(144))

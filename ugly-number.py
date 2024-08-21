# https://leetcode.com/problems/ugly-number/


# class Solution:
#     # not enough time
#     primes = set((2, 3, 5))

#     def is_prime(self, n: int):
#         if n == 1:
#             return False
#         if n in self.primes:
#             return True
#         for i in range(2, int(n ** 0.5) + 1):
#             if not n % i:
#                 return False
#         return True

#     def isUgly(self, n: int) -> bool:
#         if n < 1:
#             return False
#         if self.is_prime(n) and n not in self.primes:
#             return False
#         for i in range(1, n // 2 + 1):
#             if not n % i:
#                 if self.is_prime(i):
#                     if i not in self.primes:
#                         return False
#         return True

class Solution:
    # https://leetcode.com/problems/ugly-number/submissions/996065670/
    def successive_division(self, x: int, y: int) -> int:
        while not x % y:
            x //= y
        return x

    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        n = self.successive_division(n, 2)
        n = self.successive_division(n, 3)
        n = self.successive_division(n, 5)
        return n == 1

    def isUgly2(self, n: int) -> bool:
        # also not mine
        if n == 1:
            return True
        if n < 1:
            return False
        if not n % 5:
            n //= 5
            return self.isUgly2(n)
        if not n % 3:
            n //= 3
            return self.isUgly2(n)
        if not n % 2:
            n //= 2
            return self.isUgly2(n)
        return False


if __name__ == '__main__':
    sol = Solution()
    assert sol.isUgly2(6) is True
    assert sol.isUgly2(1) is True
    assert sol.isUgly2(14) is False
    assert sol.isUgly2(2) is True
    assert sol.isUgly2(3) is True
    assert sol.isUgly2(15) is True
    assert sol.isUgly2(11) is False

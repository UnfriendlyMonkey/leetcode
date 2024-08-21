# https://leetcode.com/problems/power-of-two/submissions/984497116/
# beats 94 in memory

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        temp = 1
        while temp <= n:
            temp *= 2
            if temp == n:
                return True
        return False

    def isPowerOfTwo2(self, n: int) -> bool:
        if n == 0:
            return False
        while not n % 2:
            n /= 2
        return n == 1

    def isPowerOfTwo3(self, n: int) -> bool:
        return n != 0 and not ('1' in bin(n)[3:])

    def isPowerOfTwo4(self, n: int) -> bool:
        # https://leetcode.com/problems/power-of-two/solutions/1638707/python-c-java-detailly-explain-why-n-n-1-works-1-line-100-faster-easy/
        # pow of 2 always like '10...0'
        # and (pow of 2) - 1 always like '01..1'
        # so bitwise and gives 0
        return n != 0 and not (n & n - 1)


sol = Solution()
assert sol.isPowerOfTwo4(16) is True
assert sol.isPowerOfTwo4(3) is False
assert sol.isPowerOfTwo4(1) is True
print(sol.isPowerOfTwo4(0))
assert sol.isPowerOfTwo4(0) is False

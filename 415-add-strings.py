# https://leetcode.com/problems/add-strings/description/
# https://leetcode.com/problems/add-strings/submissions/1368180017/
# https://leetcode.com/problems/add-strings/submissions/1368199730/
import sys


class Solution:
    def convert_to_string(self, n: int) -> str:
        if n == 0:
            return '0'
        res = ''
        while n > 0:
            n, mod = divmod(n, 10)
            res = str(mod) + res
        return res

    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)

        res = 0
        for i in range(min(len(num1), len(num2))):
            d1, d2 = int(num1[~i]), int(num2[~i])
            res += (d1 + d2) * 10 ** i
        if len(num1) > len(num2):
            for j in range(i + 1, len(num1)):
                res += int(num1[~j]) * 10 ** j
        elif len(num2) > len(num1):
            for j in range(i + 1, len(num2)):
                res += int(num2[~j]) * 10 ** j
        return str(res)
        # ValueError: Exceeds the limit (4300 digits)
        # for integer string conversion;
        # use sys.set_int_max_str_digits() to increase the limit
        res = self.convert_to_string(res)
        print(res)
        return res

    def addStrings2(self, num1: str, num2: str) -> str:
        # based upon others
        res = ''

        n1 = len(num1) - 1
        n2 = len(num2) - 1
        carry = 0

        while n1 >= 0 or n2 >= 0 or carry > 0:

            if n1 >= 0:
                carry += ord(num1[n1]) - ord('0')
                n1 -= 1
            if n2 >= 0:
                carry += ord(num2[n2]) - ord('0')
                n2 -= 1

            res = f'{carry % 10}' + res
            carry //= 10

        return res

    def addStrings3(self, num1: str, num2: str) -> str:
        # based upon others
        res = ''

        n1 = len(num1) - 1
        n2 = len(num2) - 1
        carry = 0

        while n1 >= 0 or n2 >= 0:
            s1 = int(num1[n1]) if n1 >= 0 else 0
            s2 = int(num2[n2]) if n2 >= 0 else 0

            # carry, s = divmod((s1 + s2 + carry), 10)
            s = (s1 + s2 + carry) % 10
            carry = (s1 + s2 + carry) // 10

            res = str(s) + res
            n1 -= 1
            n2 -= 1

        if carry > 0:
            res = str(carry) + res
        return res



def main():
    sol = Solution()
    num1, num2 = '11', '123'
    print(sol.addStrings(num1, num2))
    print(sol.addStrings3(num1, num2))
    num1, num2 = '456', '77'
    print(sol.addStrings(num1, num2))
    print(sol.addStrings3(num1, num2))
    num1, num2 = '0', '0'
    print(sol.addStrings(num1, num2))
    print(sol.addStrings3(num1, num2))
    num1, num2 = '1', '999999999999999'
    print(sol.addStrings(num1, num2))
    print(sol.addStrings3(num1, num2))


if __name__ == "__main__":
    main()

# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_bin = int(a, 2)
        b_bin = int(b, 2)
        return f'{a_bin + b_bin:b}'


a = '11'
b = '1'
s = Solution()
print(s.addBinary(a, b))

a = '1010'
b = '1011'
print(s.addBinary(a, b))

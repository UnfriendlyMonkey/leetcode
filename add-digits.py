# https://leetcode.com/problems/add-digits/submissions/988822632/


class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum([int(n) for n in str(num)])
        return num

    def addDigits2(self, num: int) -> int:
        # i don't understand it
        # https://leetcode.com/problems/add-digits/solutions/3458120/fully-explained-solution-with-intuition-o-1-c-must-read-once/
        # https://leetcode.com/problems/add-digits/solutions/1754049/easy-o-1-explanation-with-example/
        return 1 + (num-1) % 9 if num else 0

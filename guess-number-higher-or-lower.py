# https://leetcode.com/problems/guess-number-higher-or-lower/
# https://leetcode.com/problems/guess-number-higher-or-lower/submissions/1323273553/


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def __init__(self, guess):
        self.guess = guess

    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        if right == left:
            return right
        while right > left:
            if right - left < 2:
                return right if not guess(right) else left
            middle = left + (right - left) // 2
            res = self.guess(middle)
            print(f"{left=}, {middle=}, {right=}, {res=}")
            if res == 0:
                return middle
            if res < 0:
                right = middle
            else:
                left = middle


def main(n: int, pick: int):
    def guess(num: int):
        if num > pick:
            return -1
        elif num < pick:
            return 1
        else:
            return 0

    sol = Solution(guess)
    assert sol.guessNumber(n) == pick


if __name__ == "__main__":
    main(10, 6)
    main(101, 27)
    main(101, 2)
    main(1, 1)
    main(2, 1)

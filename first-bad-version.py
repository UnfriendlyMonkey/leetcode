# https://leetcode.com/problems/first-bad-version/submissions/992102454/
import bisect
from random import randint


bad_version = 1


def isBadVersion(version: int) -> bool:
    return version >= bad_version


def generateBadVersion(n: int) -> int:
    global bad_version
    bad_version = randint(1, n)
    # bad_version = n
    print(bad_version)


class Solution(dict):
    def firstBadVersion(self, n: int) -> int:
        generateBadVersion(n)
        if n == 1:
            return 1
        left = 1
        right = n
        while right - left > 1:
            mid = (right - left) // 2 + left
            print(left, mid, right, sep=' - ')
            if isBadVersion(mid) is True:
                right = mid
            else:
                left = mid
        return left if isBadVersion(left) is True else right

    def firstBadVersion1(self, n: int) -> int:
        # simplify my version
        generateBadVersion(n)
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            # m = (l + r) >> 1
            # the same as // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def firstBadVersion2(self, n: int) -> int:
        # doesn't work properly but idea is good
        generateBadVersion(n)
        # self.__getitem__ = isBadVersion
        return bisect.bisect_left(self, True, 1, n)

    def __getitem__(self, key):
        # necessary for second solution (as well as inheritance from dict)
        return isBadVersion(key)


sol = Solution()
print(sol.firstBadVersion1(randint(1, 99)))

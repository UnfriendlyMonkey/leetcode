# https://leetcode.com/problems/binary-watch/
from itertools import combinations


leds = [800, 400, 200, 100, 32, 16, 8, 4, 2, 1]


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []
        for r in combinations(leds, turnedOn):
            h, m = sum(r) // 100, sum(r) % 100
            # print(f"{h=}, {m=}")
            if h > 11 or m > 59:
                continue
            res.append(f"{h}:{m :02d}")
        # print(res)
        return res

    def readBinaryWatch2(self, turnedOn: int) -> list[str]:
        output = []

        def count(x):
            # don't know why it works this way
            c = 0
            while x:
                c += x % 2
                x = x // 2
            return c

        # Loop through all possible combinations of hours and minutes and count the number of set bits
        for h in range(12):
            for m in range(60):
                # Check if the number of set bits in hours and minutes equals the target number
                if count(h) + count(m) == turnedOn:
                    # Add the valid combination of hours and minutes to the output list
                    output.append(f"{h}:{m:02d}")
        return output

    def readBinaryWatch3(self, turnedOn: int) -> list[str]:
        out = []
        for h in range(12):
            for m in range(60):
                # count = m.bit_count() + h.bit_count()
                count = bin(m).count("1") + bin(h).count("1")
                if count == turnedOn:
                    out.append(f"{h}:{m:02d}")
        return out


if __name__ == "__main__":
    s = Solution()
    # s.readBinaryWatch(1)
    # s.readBinaryWatch(9)
    print(s.readBinaryWatch3(2))

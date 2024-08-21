# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
#
class Solution:
    # def twosComplement(self, num):
    #     num = num * -1
    #     res = ~num - 1
    #     print(res)
    #     print(bin(res))
    #     res_bin = bin(res)[3:]
    #     print(res_bin)
    #     res_added = f"{res_bin:1>32}"
    #     print(res_added)
    #     hex_res = hex(int(res_added, 2))
    #     print(hex_res)
    #     return hex_res[2:]

    # def toHex(self, num: int) -> str:
    #     if num == 0:
    #         return "0"
    #     if num < 0:
    #         res = self.twosComplement(num)
    #         return res
    #     if num < 0:
    # Handling negative numbers by using 32-bit unsigned representation Python's
    # bitwise operation works on signed numbers, so we convert to 32-bit
    # unsigned for negative numbers.
    #        num += 2**32
    #     hexchars = "0123456789abcdef"
    #     res = ""
    #     while num > 0:
    #         num, left = divmod(num, 16)
    #         res = hexchars[left] + res
    #     # print(res)
    #     return res

    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hexchars = "0123456789abcdef"
        res = ""
        # int is 32-bit (8 * 4)
        for _ in range(8):
            # get last 4 digits
            n = num & 15
            c = hexchars[n]
            res = c + res
            # num = num / 16
            num = num >> 4
        return res.lstrip("0")


def main():
    s = Solution()
    for num in [-1, -2, -3, -4, -5, -26, -155, -17, -72, -327856]:
        print(s.toHex(num))
    for num in [26, 155, 2, 17, 72, 327856]:
        assert s.toHex(num) == hex(num)[2:]


if __name__ == "__main__":
    main()

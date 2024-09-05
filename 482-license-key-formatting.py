# https://leetcode.com/problems/license-key-formatting/
# https://leetcode.com/problems/license-key-formatting/submissions/1379229393

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # wery slow, but memory-effective
        dash = '-'
        counter = 0
        res = ''
        for sign in s[::-1]:
            if sign == dash:
                continue
            res = (sign if sign.isdigit() else sign.upper()) + res
            counter += 1
            if not counter % k:
                res = dash + res
        return res.lstrip(dash)

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ns = s.replace('-', '', -1)



def main():
    sol = Solution()
    s = "5F3Z-2e-9-w"
    k = 4
    print(sol.licenseKeyFormatting(s, k))
    s = "2-5g-3-J"
    k = 2
    print(sol.licenseKeyFormatting(s, k))


if __name__ == "__main__":
    main()

# https://leetcode.com/problems/number-of-segments-in-a-string/
# https://leetcode.com/problems/number-of-segments-in-a-string/submissions/1378063993/

class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        splitted: list = s.split()
        return len(splitted)


def main():
    sol = Solution()
    s = "Hello, my name is John"
    print(sol.countSegments(s))
    s = "Hello"
    print(sol.countSegments(s))
    s = ""
    print(sol.countSegments(s))
    s = "!@#$%^&*()_+-=',.:"
    print(sol.countSegments(s))
    s = "!@#$ % ^&*()_ sdfff+-=',.:"
    print(sol.countSegments(s))


if __name__ == "__main__":
    main()

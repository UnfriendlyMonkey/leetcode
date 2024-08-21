# https://leetcode.com/problems/fizz-buzz/submissions/1328633820/


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        def stringer(n: int) -> str:
            # whithout function it would be faster
            if not n % 3 and not n % 5:
                return "FizzBuzz"
            if not n % 3:
                return "Fizz"
            if not n % 5:
                return "Buzz"
            return str(n)

        return [stringer(n) for n in range(1, n + 1)]


def main():
    s = Solution()
    assert s.fizzBuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]


if __name__ == "__main__":
    main()

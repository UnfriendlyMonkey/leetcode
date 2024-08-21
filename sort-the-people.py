# https://leetcode.com/problems/sort-the-people/description/?envType=daily-question&envId=2024-07-22
# https://leetcode.com/problems/sort-the-people/submissions/1329679542/
#
#
from operator import itemgetter


class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        def get_height(name) -> int:
            # Wrong! index would get wrong answer in case of same names
            return heights[names.index(name)]

        return sorted(names, key=get_height, reverse=True)

    def sortPeople1(self, names: list[str], heights: list[int]) -> list[str]:
        mixed = zip(names, heights)
        sorted_mixed = sorted(mixed, key=itemgetter(1), reverse=True)
        return [item[0] for item in sorted_mixed]


def main():
    sol = Solution()
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    print(sol.sortPeople1(names, heights))


if __name__ == "__main__":
    main()

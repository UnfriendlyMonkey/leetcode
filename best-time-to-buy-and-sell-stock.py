# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/965288133/

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = prices[0]
        diff = max - min
        min_candidate = None
        diff_candidate = 0
        for price in prices:
            if price > max:
                print('one')
                max = price
                if min_candidate is not None:
                    min = min_candidate
                    min_candidate = None
                    diff_candidate = 0
                diff = max - min
            elif price < min:
                print('two')
                if not diff:
                    print('two.one')
                    min = price
                    max = price
                elif min_candidate is None or price < min_candidate:
                    print('two.two')
                    min_candidate = price
                elif price - min_candidate > diff:
                    print('two.three')
                    max = price
                    min = min_candidate
                    diff = max - min
                    min_candidate = None
                    diff_candidate = 0
            # else:
            if (min_candidate is not None) and (price - min_candidate > diff_candidate):
                print('three')
                diff_candidate = price - min_candidate
                if diff_candidate > diff:
                    min = min_candidate
                    max = price
                    diff = max - min
                    min_candidate = None
                    diff_candidate = 0
            print(price)
            print(min, max, diff, min_candidate, diff_candidate)
        return diff


sol = Solution()

prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
# prices = [6, 9, 1, 4, 2, 7, 0, 5, 3]
# prices = [4, 7, 1, 2]

print(sol.maxProfit(prices))

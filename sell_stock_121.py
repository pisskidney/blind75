from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_score = 0
        lowest = float('inf')
        for price in prices:
            if (potential_score := price - lowest) > best_score:
                best_score = potential_score
            if lowest > price:
                lowest = price
        return best_score

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        current = res
        for num in nums[1:]:
            current = max(num, num + current)
            if res < current:
                res = current
        return res

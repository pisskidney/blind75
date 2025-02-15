from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            if current * nums[i] < nums[i]:
                current = nums[i]
            else:
                current *= nums[i]
            res = max(current, res)
        return res

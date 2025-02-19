from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_positive = nums[0]
        curr_negative = nums[0]
        for i in range(1, len(nums)):
            nr = nums[i]
            curr_positive_new = max(curr_positive * nr, curr_negative * nr, nr)
            curr_negative = min(curr_negative * nr, curr_positive * nr, nr)
            curr_positive = curr_positive_new
            res = max(curr_positive, res)
        return res

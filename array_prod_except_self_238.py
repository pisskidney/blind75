from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nr_zeros = 0
        for num in nums:
            if num == 0:
                nr_zeros += 1

        if nr_zeros > 1:
            return [0] * len(nums)

        product = 1
        for num in nums:
            if num != 0:
                product *= num

        if nr_zeros == 1:
            return [0 if x != 0 else product for x in nums]

        return [product // x for x in nums]

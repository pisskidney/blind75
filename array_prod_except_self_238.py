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
        prefix_products = []
        for num in nums:
            product *= num
            prefix_products.append(product)

        product = 1
        suffix_products = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            suffix_products[i] = product

        res = []
        for i, num in enumerate(nums):
            left = prefix_products[i-1] if i > 0 else 1
            right = suffix_products[i+1] if i < len(nums) - 1 else 1
            if i == 0:
                left = 1
            if i == len(nums) - 1:
                right = 1
            product = left * right
            res.append(product)

        return res

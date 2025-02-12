from typing import List
from operator import mul
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = reduce(mul, nums)
        return [prod / x for x in nums]

from typing import List


# 10 1 2 3 4 - 1
# 2 3 4 10 1 - 4
# 3 4 10 1 2 - 3


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] < nums[mid] < nums[right]:
                return nums[left]

            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid

            if right - left <= 1:
                return min(nums[left], nums[right])

        return nums[mid]

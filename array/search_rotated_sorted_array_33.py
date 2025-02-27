from typing import List

# 1 2 3 4 5 6 10
# 2 3 4 5 6 10 1
# 10 1 2 3 4 5 6


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] == target:
                return left

            if nums[right] == target:
                return right

            if nums[left] < nums[mid] < nums[right]:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] < nums[mid]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

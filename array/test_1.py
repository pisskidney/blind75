import pytest
from two_sum_1 import Solution


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        [
            [1, 2, 3, 4, 5],
            6,
            [1, 3]
        ],
        [
            [1, 2, 3, 2, 5],
            6,
            [0, 4]
        ],
    ]
)
def test_two_sum(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected

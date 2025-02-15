import pytest
from max_subarray_53 import Solution


@pytest.mark.parametrize(
    'nums,expected',
    [
        [
            [-1, 2, 3, -6, 2, -1, 1, 2, 3, -1, 4, 2, -3, 2],
            12
        ],
        [
            [-4],
            -4
        ],
        [
            [1, 2, 3],
            6
        ]
    ]
)
def test_max_subarray(nums, expected):
    assert Solution().maxSubArray(nums) == expected

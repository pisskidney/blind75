import pytest
from max_subarray_product_152 import Solution


@pytest.mark.parametrize(
    'nums,expected',
    [
        [
            [-2, -1, 3, 2],
            12
        ],
        [
            [2, -1, 3, 2],
            6
        ],
        [
            [-3, -1, -5],
            5
        ],
        [
            [-2, 3, -1, 5, 2, -2],
            60
        ],
        [
            [-1, 3, 0, -3, 3, 0, -1],
            3
        ]
    ]
)
def test_max_product(nums, expected):
    assert Solution().maxProduct(nums) == expected

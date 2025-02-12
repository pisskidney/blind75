import pytest
from array_prod_except_self_238 import Solution


@pytest.mark.parametrize(
    'nums,expected',
    [
        [
            [1, 2, 3, 4, 5],
            [120, 60, 40, 30, 24]
        ],
        [
            [1, 2],
            [2, 1]
        ],
        [
            [1, 1],
            [1, 1]
        ],
        [
            [1, 0, 2, 3],
            [0, 6, 0, 0]
        ],
        [
            [3, 2, 0, 0],
            [0, 0, 0, 0],
        ]
    ]
)
def test_product_except_self(nums, expected):
    assert Solution().productExceptSelf(nums) == expected

import pytest
from find_min_in_sorted_array_153 import Solution


@pytest.mark.parametrize(
    'nums,expected',
    [
        [
            [2, 3, 4, 10, 1],
            1
        ],
        [
            [3, 4, 10, 1, 2],
            1
        ],
        [
            [10, 1, 2, 3, 4],
            1
        ]
    ]
)
def test_find_min(nums, expected):
    assert Solution().findMin(nums) == expected

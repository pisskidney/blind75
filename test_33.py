import pytest
from search_rotated_sorted_array_33 import Solution


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        [
            [1, 2, 3, 4, 5, 6, 7],
            1,
            0
        ],
        [
            [1, 2, 3, 4, 5, 6, 7],
            5,
            4
        ],
        [
            [1, 2, 3, 4, 5, 6, 7],
            7,
            6
        ],
        [
            [1, 2, 3, 4, 5, 6, 7],
            5,
            4
        ],
        [
            [10, 1, 2, 3, 4],
            10,
            0
        ],
        [
            [10, 1, 2, 3, 4],
            1,
            1
        ],
        [
            [10, 1, 2, 3, 4],
            4,
            4
        ],
        [
            [10, 1, 2, 3, 4],
            44,
            -1
        ],

    ]
)
def test_search(nums, target, expected):
    assert Solution().search(nums, target) == expected

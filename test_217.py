import pytest
from contains_duplicates_217 import Solution


@pytest.mark.parametrize(
    'nums,expected',
    [
        [
            [1, 1, 2, 3, 4],
            True
        ],
        [
            [1, 4, 2, 3, 4],
            True
        ],
        [
            [1, 6, 2, 3, 4],
            False
        ],
    ]
)
def test_contains_duplicate(nums, expected):
    actual = Solution().containsDuplicate(nums)
    assert actual == expected

import pytest
from container_with_most_water_11 import Solution


@pytest.mark.parametrize(
    'height,expected',
    [
        [
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            49
        ],
        [
            [1, 2],
            1
        ],
        [
            [1, 10, 1],
            2
        ],
    ]
)
def test_max_area(height, expected):
    assert Solution().maxArea(height) == expected

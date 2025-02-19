import pytest
from spiral_matrix_54 import Solution


@pytest.mark.parametrize(
    'matrix,expected',
    [
        [
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ],
        [
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        ],
        [
            [[1, 2], [3, 4]],
            [1, 2, 4, 3]
        ]
    ]
)
def test_spiral_order(matrix, expected):
    assert Solution().spiralOrder(matrix) == expected

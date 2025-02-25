import pytest
from word_search_79 import Solution


@pytest.mark.parametrize(
    'board,word,expected',
    [
        [
            [["A", "B", "C", "E"],["S", "F", "C", "S"],["A", "D", "E", "E"]],
            'ABCCED',
            True
        ],
        [
            [["A", "B", "C", "E"],["S", "F", "C", "S"],["A", "D", "E", "E"]],
            'ABCCEX',
            False
        ],
    ]
)
def test_exist(board, word, expected):
    assert Solution().exist(board, word) == expected

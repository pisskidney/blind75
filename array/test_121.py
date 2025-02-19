import pytest
from sell_stock_121 import Solution


@pytest.mark.parametrize(
    'prices,expected',
    [
        [
            [1, 2, 4, 5, 6],
            5,
        ],
        [
            [3, 2, 1],
            0,
        ],
        [
            [3, 2, 1, 0, 4, 0, 7],
            7,
        ]
    ]
)
def test_max_profit(prices, expected):
    result = Solution().maxProfit(prices)
    assert result == expected

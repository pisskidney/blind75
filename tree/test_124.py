import pytest
from binary_tree_max_path_sum_124 import TreeNode, Solution


@pytest.fixture
def trees():
    root0 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    root1 = TreeNode(-3)
    root2 = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))
    root3 = TreeNode(-1, TreeNode(-2, TreeNode(-6)), TreeNode(10, TreeNode(-3), TreeNode(-6)))
    return [root0, root1, root2, root3]


@pytest.mark.parametrize(
    'tree_index, expected',
    [
        [
            0,
            42
        ],
        [
            1,
            -3
        ],
        [
            2,
            3
        ],
        [
            3,
            10
        ]
    ]
)
def test_maxPathSum(trees, tree_index, expected):
    assert Solution().maxPathSum(trees[tree_index]) == expected

from awesome_python_leetcode._173_binary_search_tree_iterator import (
    BSTIterator,
    TreeNode,
)


def test_func():
    root = TreeNode.build([7, 3, 15, None, None, 9, 20])
    iterator = BSTIterator(root)
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext() is True
    assert iterator.next() == 9
    assert iterator.hasNext() is True
    assert iterator.next() == 15
    assert iterator.hasNext() is True
    assert iterator.next() == 20
    assert iterator.hasNext() is False

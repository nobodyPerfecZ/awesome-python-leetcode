from awesome_python_leetcode._380_insert_delete_getrandom_o_1 import RandomizedSet


def test_func():
    """Tests the solution of a LeetCode problem."""
    randomSet = RandomizedSet()
    assert randomSet.insert(1) is True
    assert randomSet.remove(2) is False
    assert randomSet.insert(2) is True
    assert randomSet.getRandom() in [1, 2]
    assert randomSet.remove(1) is True
    assert randomSet.insert(2) is False
    assert randomSet.getRandom() == 2

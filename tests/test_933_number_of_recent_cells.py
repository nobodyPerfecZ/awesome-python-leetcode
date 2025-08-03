from awesome_python_leetcode._933_number_of_recent_calls import RecentCounter


def test_func():
    """Tests the solution of a LeetCode problem."""
    counter = RecentCounter()
    assert 1 == counter.ping(1)
    assert 2 == counter.ping(100)
    assert 3 == counter.ping(3001)
    assert 3 == counter.ping(3002)

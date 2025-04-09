from awesome_python_leetcode._295_find_median_from_data_stream import MedianFinder


def test_func():
    """Tests the solution of a LeetCode problem."""
    finder = MedianFinder()
    finder.addNum(1)
    finder.addNum(2)
    assert finder.findMedian() == 1.5
    finder.addNum(3)
    assert finder.findMedian() == 2

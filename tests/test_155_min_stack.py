from awesome_python_leetcode._155_min_stack import MinStack


def test_func():
    """Tests the solution of a LeetCode problem."""
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2

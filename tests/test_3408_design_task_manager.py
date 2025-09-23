from awesome_python_leetcode._3408_design_task_manager import TaskManager


def test_func():
    """Tests the solution of a LeetCode problem."""
    manager = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])

    manager.add(4, 104, 5)
    manager.edit(102, 8)
    assert manager.execTop() == 3

    manager.rmv(101)
    manager.add(5, 105, 15)
    assert manager.execTop() == 5

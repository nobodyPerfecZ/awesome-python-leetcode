from awesome_python_leetcode._1912_design_movie_rental_system import MovieRentingSystem


def test_func():
    """Tests the solution of a LeetCode problem."""
    system = MovieRentingSystem(
        3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]
    )
    assert system.search(1) == [1, 0, 2]

    system.rent(0, 1)
    system.rent(1, 2)
    assert system.report() == [[0, 1], [1, 2]]

    system.drop(1, 2)
    assert system.search(2) == [0, 1]

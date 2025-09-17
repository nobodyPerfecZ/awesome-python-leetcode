from awesome_python_leetcode._2353_design_a_food_rating_system import FoodRatings


def test_func():
    """Tests the solution of a LeetCode problem."""
    food_ratings = FoodRatings(
        foods=["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        cuisines=["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        ratings=[9, 12, 8, 15, 14, 7],
    )
    assert food_ratings.highestRated("korean") == "kimchi"
    assert food_ratings.highestRated("japanese") == "ramen"

    food_ratings.changeRating("sushi", 16)
    assert food_ratings.highestRated("japanese") == "sushi"

    food_ratings.changeRating("ramen", 16)
    assert food_ratings.highestRated("japanese") == "ramen"

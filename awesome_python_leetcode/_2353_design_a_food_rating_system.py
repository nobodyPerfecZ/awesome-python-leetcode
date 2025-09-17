import collections
import heapq
from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class Food:
    """Item stored in the priority queue."""

    rating: int = field(compare=True)
    food: str = field(compare=True)
    cuisine: str = field(compare=False)


class FoodRatings:
    """
    Design a food rating system that can do the following:
    - Modify the rating of a food item listed in the system.
    - Return the highest-rated food item for a type of cuisine in the system.

    Implement the FoodRatings class:
    - FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the
    system. The food items are described by foods, cuisines and ratings, all of which
    have a length of n.
        - foods[i] is the name of the ith food,
        - cuisines[i] is the type of cuisine of the ith food, and
        - ratings[i] is the initial rating of the ith food.
    - void changeRating(String food, int newRating) Changes the rating of the food item
    with the name food.
    - String highestRated(String cuisine) Returns the name of the food item that has the
    highest rating for the given type of cuisine. If there is a tie, return the item
    with the lexicographically smaller name.

    Note that a string x is lexicographically smaller than string y if x comes before y
    in dictionary order, that is, either x is a prefix of y, or if i is the first
    position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
    """

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_max_food = collections.defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings, strict=False):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = -r
            heapq.heappush(self.cuisine_to_max_food[c], Food(-r, f, c))

    def changeRating(self, food: str, newRating: int) -> None:
        # Update food_to_rating
        self.food_to_rating[food] = -newRating

        # Insert the new food element in the priority queue
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(
            self.cuisine_to_max_food[cuisine], Food(-newRating, food, cuisine)
        )

    def highestRated(self, cuisine: str) -> str:
        # Get the highest rated food of
        max_food = self.cuisine_to_max_food[cuisine][0]

        while self.food_to_rating[max_food.food] != max_food.rating:
            heapq.heappop(self.cuisine_to_max_food[cuisine])
            max_food = self.cuisine_to_max_food[cuisine][0]

        return max_food.food

import collections
import heapq
from typing import List


class MovieRentingSystem:
    """
    You have a movie renting company consisting of n shops. You want to implement a
    renting system that supports searching for, booking, and returning movies. The
    system should also support generating a report of the currently rented movies.

    Each movie is given as a 2D integer array entries where entries[i] =
    [shopi, moviei, pricei] indicates that there is a copy of movie moviei at shop
    shopi with a rental price of pricei. Each shop carries at most one copy of a movie
    moviei.

    The system should support the following functions:
    - Search: Finds the cheapest 5 shops that have an unrented copy of a given movie.
    The shops should be sorted by price in ascending order, and in case of a tie, the
    one with the smaller shopi should appear first. If there are less than 5 matching
    shops, then all of them should be returned. If no shop has an unrented copy, then
    an empty list should be returned.
    - Rent: Rents an unrented copy of a given movie from a given shop.
    - Drop: Drops off a previously rented copy of a given movie at a given shop.
    - Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a
    2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented
    movie moviej was rented from the shop shopj. The movies in res should be sorted by
    price in ascending order, and in case of a tie, the one with the smaller shopj
    should appear first, and if there is still tie, the one with the smaller moviej
    should appear first. If there are fewer than 5 rented movies, then all of them
    should be returned. If no movies are currently being rented, then an empty list
    should be returned.

    Implement the MovieRentingSystem class:
    - MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem
    object with n shops and the movies in entries.
    - List<Integer> search(int movie) Returns a list of shops that have an unrented copy
    of the given movie as described above.
    - void rent(int shop, int movie) Rents the given movie from the given shop.
    - void drop(int shop, int movie) Drops off a previously rented movie at the given
    shop.
    - List<List<Integer>> report() Returns a list of cheapest rented movies as describe
    above.

    Note: The test cases will be generated such that rent will only be called if the
    shop has an unrented copy of the movie, and drop will only be called if the shop
    had previously rented out the movie.
    """

    def __init__(self, n: int, entries: List[List[int]]):
        # Dictionary
        # Key: (Shop, Movie)
        # Value: Price
        self.shop_movie_to_price = collections.defaultdict(dict)

        # Dictionary
        # Key: Movie
        # Value: RentingItem
        self.unrented_movie_to_item = collections.defaultdict(list)

        # RentingItem
        self.rented_item = []

        # Sets for managing hashmaps as we cannot remove non-top items
        self.rented = set()
        self.returned = set()

        for entry in entries:
            shop, movie, price = entry
            self.shop_movie_to_price[shop][movie] = price
            heapq.heappush(self.unrented_movie_to_item[movie], (price, shop, movie))

    def search(self, movie: int) -> List[int]:
        # Get the 5 cheapest shops
        res = []
        items = []
        while self.unrented_movie_to_item[movie] and len(res) < 5:
            while (
                self.unrented_movie_to_item[movie]
                and self.unrented_movie_to_item[movie][0] in self.rented
            ):
                item = heapq.heappop(self.unrented_movie_to_item[movie])
                self.rented.remove(item)
            if self.unrented_movie_to_item[movie]:
                item = heapq.heappop(self.unrented_movie_to_item[movie])
                res.append(item[1])
                items.append(item)

        # Append the 5 cheapest shops
        for item in items:
            heapq.heappush(self.unrented_movie_to_item[movie], item)
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_to_price[shop][movie]
        item = (price, shop, movie)
        self.rented.add(item)
        if item in self.returned:
            self.returned.remove(item)
        else:
            # Push the new rented item to the list of rented items
            heapq.heappush(self.rented_item, item)

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie_to_price[shop][movie]
        item = (price, shop, movie)
        self.returned.add(item)
        if item in self.rented:
            self.rented.remove(item)
        else:
            # Push the new not rented item to the list of non-rented items
            heapq.heappush(self.unrented_movie_to_item[movie], item)

    def report(self) -> List[List[int]]:
        # Get the 5 cheapest rented movies
        res = []
        items = []
        while self.rented_item and len(res) < 5:
            while self.rented_item and self.rented_item[0] in self.returned:
                item = heapq.heappop(self.rented_item)
                self.returned.remove(item)
            if self.rented_item:
                item = heapq.heappop(self.rented_item)
                res.append([item[1], item[2]])
                items.append(item)

        # Append the 5 cheapest movies
        for item in items:
            heapq.heappush(self.rented_item, item)
        return res


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

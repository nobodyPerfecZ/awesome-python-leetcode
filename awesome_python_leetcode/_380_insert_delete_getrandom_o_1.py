import random


class RandomizedSet:
    """
    Implement the RandomizedSet class:
    - RandomizedSet() Initializes the RandomizedSet object.
    - bool insert(int val) Inserts an item val into the set if not present. Returns true
    if the item was not present, false otherwise.
    - bool remove(int val) Removes an item val from the set if present. Returns true if
    the item was present, false otherwise.
    - int getRandom() Returns a random element from the current set of elements (it's
    guaranteed that at least one element exists when this method is called). Each
    element must have the same probability of being returned.

    You must implement the functions of the class such that each function works in
    average O(1) time complexity.
    """

    def __init__(self):
        self.value_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.value_to_index:
            return False
        else:
            self.value_to_index[val] = len(self.values)
            self.values.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_index:
            return False
        else:
            idx = self.value_to_index[val]
            last_idx = len(self.values) - 1
            self.value_to_index[self.values[last_idx]] = idx
            self.values[idx], self.values[last_idx] = (
                self.values[last_idx],
                self.values[idx],
            )
            self.values.pop()
            del self.value_to_index[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.values)

from typing import Dict


class WordDictionary:
    """
    Design a data structure that supports adding new words and finding if a string
    matches any previously added string.

    Implement the WordDictionary class:
    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure, it can be matched later.
    - bool search(word) Returns true if there is any string in the data structure that
    matches word or false otherwise. word may contain dots '.' where dots can be
    matched with any letter.
    """

    def __init__(
        self,
        val: str = None,
        end: bool = False,
        letters: Dict[str, "WordDictionary"] = None,
    ):
        self.val = val
        self.end = end
        self.letters = letters if letters is not None else {}

    def addWord(self, word: str) -> None:
        parent = self
        for i, c in enumerate(word, 1):
            end = i == len(word)
            if c not in parent.letters:
                parent.letters[c] = WordDictionary(val=c)
            if end:
                parent.letters[c].end = end
            parent = parent.letters[c]

    def search(self, word: str) -> bool:
        parent = self
        for i, c in enumerate(word):
            if c == ".":
                found = False
                for c_ in parent.letters:
                    found = found | parent.letters[c_].search(word[i + 1 :])
                return found
            elif c not in parent.letters:
                return False
            parent = parent.letters[c]
        return parent.end

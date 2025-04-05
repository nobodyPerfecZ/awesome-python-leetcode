from typing import Dict


class Trie:
    """
    A trie (pronounced as "try") or prefix tree is a tree data structure used to
    efficiently store and retrieve keys in a dataset of strings. There are various
    applications of this data structure, such as autocomplete and spellchecker.

    Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie
    (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously inserted
    string word that has the prefix prefix, and false otherwise.
    """

    def __init__(
        self,
        val: str = None,
        end: bool = False,
        letters: Dict[str, "Trie"] = None,
    ):
        self.val = val
        self.end = end
        self.letters = letters if letters is not None else {}

    def insert(self, word: str) -> None:
        parent = self
        for i, c in enumerate(word, 1):
            end = i == len(word)
            if c not in parent.letters:
                parent.letters[c] = Trie(val=c)
            if end:
                parent.letters[c].end = end
            parent = parent.letters[c]

    def search(self, word: str) -> bool:
        parent = self
        for c in word:
            if c not in parent.letters:
                return False
            parent = parent.letters[c]
        return parent.end

    def startsWith(self, prefix: str) -> bool:
        parent = self
        for c in prefix:
            if c not in parent.letters:
                return False
            parent = parent.letters[c]
        return True

from typing import Dict, List


class Trie:
    def __init__(self, end: bool = False, letters: Dict[str, "Trie"] = None):
        self.end = end
        self.children = letters if letters is not None else {}

    def insert(self, word: str) -> None:
        parent = self
        for c in word:
            if c not in parent.children:
                parent.children[c] = Trie()
            parent = parent.children[c]
        parent.end = True


class Solution:
    """Base class for all LeetCode Problems."""

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Given an m x n board of characters and a list of strings words, return all words
        on the board.

        Each word must be constructed from letters of sequentially adjacent cells,
        where adjacent cells are horizontally or vertically neighboring. The same
        letter cell may not be used more than once in a word.
        """

        root = Trie()
        for word in words:
            root.insert(word)

        res, path = set(), set()

        def dfs(row: int, col: int, node: Trie, word: str):
            if (
                row < 0
                or row >= len(board)
                or col < 0
                or col >= len(board[0])
                or board[row][col] not in node.children
                or (row, col) in path
            ):
                return False
            path.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.end:
                res.add(word)
            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)
            path.remove((row, col))
            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, root, "")
        return list(res)

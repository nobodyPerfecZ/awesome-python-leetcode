import collections
from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        A transformation sequence from word beginWord to word endWord using a dictionary
        wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
        - Every adjacent pair of words differs by a single letter.
        - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
        be in wordList.
        - sk == endWord

        Given two words, beginWord and endWord, and a dictionary wordList, return the
        number of words in the shortest transformation sequence from beginWord to
        endWord, or 0 if no such sequence exists.
        """
        # Create adjacency matrix
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                adj[pattern].append(word)

        def bfs(src, target):
            queue = [(src, 1)]
            visited = {src}
            while queue:
                word, mutations = queue.pop(0)
                if word == target:
                    return mutations
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for next_word in adj[pattern]:
                        if next_word not in visited:
                            queue.append((next_word, mutations + 1))
                            visited.add(next_word)
            return 0

        return bfs(beginWord, endWord)

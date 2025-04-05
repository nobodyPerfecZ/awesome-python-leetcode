from awesome_python_leetcode._211_design_add_and_search_words_data_structure import (
    WordDictionary,
)


def test_func():
    """Tests the solution of a LeetCode problem."""
    wordDict = WordDictionary()
    wordDict.addWord("bad")
    wordDict.addWord("dad")
    wordDict.addWord("mad")
    assert wordDict.search("pad") is False
    assert wordDict.search("bad") is True
    assert wordDict.search(".ad") is True
    assert wordDict.search("b..") is True

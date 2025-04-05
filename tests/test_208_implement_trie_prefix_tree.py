from awesome_python_leetcode._208_implement_trie_prefix_tree import Trie


def test_func():
    """Tests the solution of a LeetCode problem."""
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True

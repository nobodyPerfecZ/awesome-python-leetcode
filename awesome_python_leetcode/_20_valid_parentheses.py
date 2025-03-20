class Solution:
    """Base class for all LeetCode Problems."""

    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
        """
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            elif not stack:
                return False
            else:
                open_bracket = stack.pop()
                closed_bracket = brackets[open_bracket]
                if closed_bracket != bracket:
                    return False
        return not stack

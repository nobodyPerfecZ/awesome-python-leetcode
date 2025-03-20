from typing import List


class Solution:
    """Base class for all LeetCode Problems."""

    def evalRPN(self, tokens: List[str]) -> int:
        """
        You are given an array of strings tokens that represents an arithmetic
        expression in a Reverse Polish Notation.

        Evaluate the expression. Return an integer that represents the value of the
        expression.

        Note that:
        - The valid operators are '+', '-', '*', and '/'.
        - Each operand may be an integer or another expression.
        - The division between two integers always truncates toward zero.
        - There will not be any division by zero.
        - The input represents a valid arithmetic expression in a reverse polish
        notation.
        - The answer and all the intermediate calculations can be represented in a
        32-bit integer.
        """
        stack = []
        for t in tokens:
            if t == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first + second))
            elif t == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first * second))
            elif t == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first - second))
            elif t == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(t))
        return stack[0]

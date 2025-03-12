class Solution:
    def calculate(self, s: str) -> int:
        """
        Given a string s which represents an expression,
        evaluate this expression and return its value.

        The integer division should truncate toward zero.

        You may assume that the given expression is always valid.
        All intermediate results will be in the range of [-231, 231 - 1].

        Note: You are not allowed to use any built-in function which
        evaluates strings as mathematical expressions, such as eval().
        """
        prev, cur, res, op, i = 0, 0, 0, "+", 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1
                if op == "+":
                    res += cur
                    prev = cur
                elif op == "-":
                    res -= cur
                    prev = -cur
                elif op == "*":
                    res -= prev
                    res += prev * cur
                    prev = cur * prev
                elif op == "/":
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)

                cur = 0
            elif c != " ":
                op = c
            i += 1
        return res

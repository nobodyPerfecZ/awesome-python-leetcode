class Solution:
    def calculate(self, s: str) -> int:
        """
        Given a string s representing a valid expression,
        implement a basic calculator to evaluate it,
        and return the result of the evaluation.

        Note: You are not allowed to use any built-in function
        which evaluates strings as mathematical
        expressions, such as eval().
        """
        stack = []
        cur, res, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in ["+", "-"]:
                res += sign * cur
                cur = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append((res, sign))
                res, sign = 0, 1
            elif c == ")":
                res += sign * cur
                i_res, i_sign = stack.pop()
                res *= i_sign
                res += i_res
                cur = 0
        return res + sign * cur

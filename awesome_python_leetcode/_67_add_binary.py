class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Given two binary strings a and b, return their sum as a binary string."""
        result, overhead = "", "0"
        max_length = max(len(a), len(b))
        a = ("0" * (max_length - len(a))) + a
        b = ("0" * (max_length - len(b))) + b
        for a_, b_ in zip(reversed(a), reversed(b)):
            if a_ == "0" and b_ == "0" and overhead == "0":
                result = "0" + result
                overhead = "0"
            elif a_ == "0" and b_ == "0" and overhead == "1":
                result = "1" + result
                overhead = "0"
            elif a_ == "0" and b_ == "1" and overhead == "0":
                result = "1" + result
                overhead = "0"
            elif a_ == "0" and b_ == "1" and overhead == "1":
                result = "0" + result
                overhead = "1"
            elif a_ == "1" and b_ == "0" and overhead == "0":
                result = "1" + result
                overhead = "0"
            elif a_ == "1" and b_ == "0" and overhead == "1":
                result = "0" + result
                overhead = "1"
            elif a_ == "1" and b_ == "1" and overhead == "0":
                result = "0" + result
                overhead = "1"
            elif a_ == "1" and b_ == "1" and overhead == "1":
                result = "1" + result
                overhead = "1"
        return overhead + result if overhead == "1" else result

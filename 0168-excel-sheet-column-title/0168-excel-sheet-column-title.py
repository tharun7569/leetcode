class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            n -= 1
            result = chr(ord('A') + n % 26) + result
            n //= 26
        return result

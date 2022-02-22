class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for a in columnTitle:
            c = ord(a)-ord('@')
            result = result*26 + c
        return result

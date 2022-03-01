class Solution:
    def countBits(self, n: int) -> List[int]:
        stack = []
        for i in range(n+1):
            a = bin(i)[2:]
            sum = 0
            for digit in str(a):
                sum+=int(digit)
            stack.append(sum)
        return stack

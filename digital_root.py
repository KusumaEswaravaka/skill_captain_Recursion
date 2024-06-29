class Solution:
    def sumDigits(self, n: int) -> int:
        if n // 10 == 0:  # checks whether the number is a single digit or not
            return n
        else:
            return (n % 10) + self.sumDigits(n // 10)
    
    def digitalRoot(self, n: int) -> int:
        if n // 10 == 0:
            return n
        else:
            return self.digitalRoot(self.sumDigits(n))
    
    def digitalRoots(self, numbers: list) -> list:
        return [self.digitalRoot(n) for n in numbers]

# Example usage
solution = Solution()
numbers = [99999, 493, 56, 8]
results = solution.digitalRoots(numbers)
print("Outputs:", results)

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number: int = 0
        size: int = len(digits)
        for i, digit in enumerate(digits):
            number += digit * pow(10, size - 1 - i)
        return list(map(int, str(number + 1)))
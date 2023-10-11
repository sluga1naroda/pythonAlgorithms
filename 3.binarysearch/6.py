class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return divmod(dividend, divisor)[0]

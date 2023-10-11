import math
class Solution:
    def estimateBudget(self, n: int, k: int) -> int:
        return (int(math.log2(n))+1)*k

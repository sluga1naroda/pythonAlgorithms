class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        head = -1
        tail = len(letters)-1
        while True:
            if tail-head<=1:
                return letters[tail]
            mid = (head + tail) // 2
            if letters[mid] <= target:
                head = mid
                continue
            elif letters[mid] > target and letters[mid-1] > target:
                tail = mid
                continue
            elif letters[mid] > target and letters[mid-1] <= target:
                return letters[mid]
        return 'shit'

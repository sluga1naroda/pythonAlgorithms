class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid + 1) == True and isBadVersion(mid) == False:
                return mid + 1
            elif isBadVersion(mid + 1) == False:
                l = mid + 1
            else:
                r = mid - 1
        return l + 1
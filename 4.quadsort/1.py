class Solution:
    def bubbleSwapCount(self, A) -> int:
        cnt=0
        N = len(A)
        for i in range(N-1):
            for j in range(N-i-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
                    cnt+=1

        return cnt

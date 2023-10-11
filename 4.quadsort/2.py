class Solution:
    def bubbleSwap(self, A) -> int:
        N = len(A)
        for i in range(N-1):
            for j in range(N-i-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
        return A

    def sortArray(self, A):
        e = []
        o = []
        ans = []
        for i in A:
            if i%2 == 0:
                e.append(i)
            else:
                o.append(i)
        e = self.bubbleSwap(e)
        o = self.bubbleSwap(o)[::-1]
        for i in range(len(e)):
            ans.append(e[i])
            ans.append(o[i])
        return ans

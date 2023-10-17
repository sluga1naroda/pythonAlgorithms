class Solution:
    def largestPerimeter(self, A) -> int:
        l = len(A) - 1 
        pere = True
        i = 0
        while pere:
            pere = False
            for k in range(l):
                if A[k] < A[k+1]:
                    A[k], A[k+1] = A[k+1], A[k]
                    i += 1
                    pere = True
            l -= 1
        #print(A)
        for j in range(len(A)):
            j = 0
            while A[j] >= A[j+1] + A[j+2]:
                j += 1
           
        return A[j] + A[j+1] + A[j+2]

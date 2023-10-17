class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        
        for i in range(len(s)):    
            min_i = i
            for k in range(i + 1, len(s)):
                if s[k] < s[min_i]:
                    min_i = k
            s[i], s[min_i] = s[min_i], s[i]

        for i in range(len(t)):
            min_i = i
            for a in range(i + 1, len(t)):
                if t[a] < t[min_i]:
                    min_i = a
            t[i], t[min_i] = t[min_i], t[i]

        if t == s:
            return True
        else:
            return False
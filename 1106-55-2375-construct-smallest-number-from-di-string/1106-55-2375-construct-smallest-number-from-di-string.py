class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = "".join([str(i) for i in range(1,n+2)])
        i=0
        while i<n:
            if pattern[i]=='D':
                r = i
                while r<n and pattern[r]=='D':
                    r+=1
                res = res[:i]+res[i:r+1][::-1]+res[r+1:]
                i=r-1
            i+=1
        return res

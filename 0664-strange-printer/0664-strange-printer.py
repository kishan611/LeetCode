class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def helper(i,j):
            if i==j:
                return 1
            if s[i]==s[j]:
                return helper(i,j-1)
            res=helper(i,j-1)+1
            k=i+1
            while k<j-1:
                if s[k]==s[j]:
                    res=min(res,helper(i,k-1)+helper(k,j-1))
                    k+=1
                k+=1
            return res
        s=[c for c,_ in groupby(s)]
        return helper(0,len(s)-1)
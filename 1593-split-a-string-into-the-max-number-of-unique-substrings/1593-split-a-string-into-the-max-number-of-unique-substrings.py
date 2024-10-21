class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(i,sn):
            if i==len(s):
                return 0
            res=0
            for e in range(i+1,len(s)+1):
                ss=s[i:e]
                if ss not in sn:
                    sn.add(ss)
                    res=max(res,1+helper(e,sn))
                    sn.remove(ss)
            return res
        return helper(0,set())
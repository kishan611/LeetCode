class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1={}
        d2={}
        res=[]
        for i in p:
            d1[i]=d1.get(i,0)+1
        n1=len(p)
        n2=len(s)
        if n1>n2:
            return []
        for i in range(n1):
            d2[s[i]]=d2.get(s[i],0)+1
        if d1==d2:
            res.append(0)
        for i in range(n1,n2):
            if d2.get(s[i-n1],0)==1:
                del d2[s[i-n1]]
            else:
                d2[s[i-n1]]-=1
            d2[s[i]]=d2.get(s[i],0)+1
            if d1==d2:
                res.append(i-n1+1)
        return res
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        d=sorted(d.items(),key=lambda x:x[1],reverse=True)
        s=""
        for i in d:
            s+=i[0]*i[1]
        return s   
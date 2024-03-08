class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        m=0
        for i in nums:
            d[i]=d.get(i,0)+1
            m=max(m,d[i])
        c=0
        for i,j in d.items():
            if j==m:
                c+=1
        return c*m
        
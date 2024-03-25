class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if d.get(i,0):
                d[i]+=1
            else:
                d[i]=1
        return [i for i,j in d.items() if j>=2]
            
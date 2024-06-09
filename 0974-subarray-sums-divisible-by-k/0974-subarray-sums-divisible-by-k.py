class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count,curr=0,0
        d={0:1}
        for i in nums:
            curr=(curr+i)%k
            if curr<0:
                curr=k
            if d.get(curr,0):
                count+=d[curr]
            d[curr]=d.get(curr,0)+1
        return count
            
        
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start=0
        d={}
        count=0
        for i in nums:
            if d.get(i,0):
                if d[i]+1>k:
                    count=max(count,sum(d.values()))
                    while nums[start]!=i:
                        d[nums[start]]-=1
                        start+=1
                    start+=1
                else:
                    d[i]+=1
            else:
                d[i]=1
        count=max(count,sum(d.values()))
        return count
                        
        
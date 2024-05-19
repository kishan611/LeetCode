class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total=sum(nums)
        extra=0
        count=0
        min_diff=float("inf")
        for i in nums:
            diff=(i^k)-i
            if diff>0:
                extra+=diff
                count+=1
            min_diff=min(min_diff,abs(diff))
        if count%2==1:
            extra-=min_diff
        return total+extra
            
        
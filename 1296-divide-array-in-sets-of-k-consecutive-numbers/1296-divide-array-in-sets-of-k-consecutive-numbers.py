from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n=len(nums)            
        if n%k!=0:
            return False
        nums=Counter(nums)
        while nums:
            x=min(nums)
            for i in range(x,x+k):
                if nums.get(i,0)==0:
                    return False
                nums[i]-=1
                if nums[i]==0:
                    del nums[i]
        return True
        
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        flip=0
        res=0
        for i in range(n):
            if i>=k:
                x=1 if nums[i-k]==-1 else 0
                flip^=x
            if flip==nums[i]:
                if i+k>n:
                    return -1
                flip^=1
                nums[i]=-1
                res+=1
        return res
                
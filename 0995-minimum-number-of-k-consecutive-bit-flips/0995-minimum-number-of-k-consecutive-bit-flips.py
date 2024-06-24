class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n=len(nums)
        flip=0
        add=[0]*n
        res=0
        for i in range(n):
            if i>=k:
                flip^=add[i-k]
            if flip==nums[i]:
                if i+k>n:
                    return -1
                flip^=1
                add[i]=1
                res+=1
        return res
                
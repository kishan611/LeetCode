class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(i,cx,n):
            if i==n:
                return cx
            x1=xor(i+1,nums[i]^cx,n)
            x2=xor(i+1,cx,n)
            return x1+x2
        return xor(0,0,len(nums))
        
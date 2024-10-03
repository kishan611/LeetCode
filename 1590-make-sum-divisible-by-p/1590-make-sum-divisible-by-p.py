class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        tr = s % p
        if tr == 0:
            return 0
        ps = 0
        res = len(nums)
        rm = {0: -1}  
        for i, num in enumerate(nums):
            ps = (ps + num) % p
            rr = (ps - tr) % p
            
            if rr in rm:
                res = min(res, i - rm[rr])
            rm[ps] = i
        return res if res < len(nums) else -1
            
        
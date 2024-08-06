class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res=nums[0]
        dis=abs(res)
        for i in nums[1::]:
            if abs(i)<dis:
                dis=abs(i)
                res=i
            elif abs(i)==dis:
                if i>res:
                    res=i
        return res
                
        
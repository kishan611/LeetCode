class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res=nums[::]
        for i in range(len(nums)):
            curr=nums[i]
            for j in nums[i+1::]:
                curr+=j
                res.append(curr)
        res.sort()
        return sum(res[left-1:right])%(10**9+7)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup=set()
        n=len(nums)+1
        for i in range(n-1):
            index=nums[i]%n
            nums[index-1]+=n
            if nums[index-1]//n>=2:
                dup.add(index)
        return dup
            
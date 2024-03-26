from collections import Counter 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        c=Counter(nums)
        for i in range(len(nums)):
            if i+1 not in c:
                return i+1
        return len(nums)+1
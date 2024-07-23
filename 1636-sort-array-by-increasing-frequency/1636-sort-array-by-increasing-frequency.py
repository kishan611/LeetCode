from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        return sorted(nums,key=lambda x:(d[x],-x))
        
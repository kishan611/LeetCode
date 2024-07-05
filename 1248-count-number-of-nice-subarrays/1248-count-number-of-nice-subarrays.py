class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        l=0
        curr_count=0
        pre_count=0
        for r in range(len(nums)):
            if nums[r]&1:
                curr_count+=1
                pre_count=0
            while curr_count==k:
                if nums[l]&1:
                    curr_count-=1
                pre_count+=1
                l+=1
            count+=pre_count
        return count
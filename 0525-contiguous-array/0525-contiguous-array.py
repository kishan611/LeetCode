class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={}
        curr_sum=0
        max_len=0
        for index,value in enumerate(nums):
            curr_sum+=1 if value==1 else -1
            if curr_sum==0:
                max_len=index+1
            elif curr_sum in d:
                max_len=max(max_len,index-d[curr_sum])
            else:
                d[curr_sum]=index
        return max_len
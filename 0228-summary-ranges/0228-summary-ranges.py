class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res=[]
        start=end=nums[0]
        for i in nums[1:]:
            if i==end+1:
                end=i
            else:
                if start==end:
                    res.append(str(start))
                else:
                    res.append(f'{start}->{end}')
                start=end=i
        if start==end:
            res.append(str(start))
        else:
            res.append(f'{start}->{end}')
        return res
        
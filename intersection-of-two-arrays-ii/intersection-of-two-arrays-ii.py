class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n,m=len(nums1),len(nums2)
        d={}
        res=[]
        if n<m:
            for i in nums1:
                d[i]=d.get(i,0)+1
            for i in nums2:
                if i in d and d[i]>0:
                    res.append(i)
                    d[i]-=1
        else:
            for i in nums2:
                d[i]=d.get(i,0)+1
            for i in nums1:
                if i in d and d[i]>0:
                    res.append(i)
                    d[i]-=1
        return res
            
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        l=[]
        d={}
        count=0
        for i in range(n-1,-1,-1):
            while count and l[-1]<=nums2[i]:
                l.pop()
                count-=1
            d[nums2[i]]=l[-1] if count else -1
            l.append(nums2[i])
            count+=1
        l=[]
        for i in nums1:
            l.append(d[i])
        return l
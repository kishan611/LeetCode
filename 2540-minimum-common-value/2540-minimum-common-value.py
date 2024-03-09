class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        n,m=len(nums1),len(nums2)
        while i<n and j<m:
            if nums1[i]==nums2[j]:
                return nums1[i]
            if nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return -1
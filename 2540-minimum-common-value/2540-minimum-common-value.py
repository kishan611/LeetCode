class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        j=0
        n=len(nums2)
        for i in nums1:
            print(i,j)
            if j<n:
                if i==nums2[j]:
                    return i
                if i<nums2[j]:
                    continue
                while j<n and nums2[j]<i:
                    j+=1
                else:
                    if j<n and nums2[j]==i:
                        return i
            else:
                return -1
        return -1
                
            
        
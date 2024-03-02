class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        neg=[]
        nc=0
        for i in nums:
            if i<0:
                neg.append(i*i)
                nc+=1
            else:
                break
        nums=[x*x for x in nums[nc:]]
        neg.reverse()
        i
        j=0
        for i in neg:
            while j<n-nc and i>nums[j]:
                j+=1
            else:
                nums.insert(j,i)
                j+=1
                nc-=1
        return nums
            
            
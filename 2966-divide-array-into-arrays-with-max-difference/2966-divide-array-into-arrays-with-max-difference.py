class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res=[[nums[0]]]
        j=1
        for i in range(1,len(nums)):
            if j==1:
                if nums[i]-nums[i-1]<=k:
                    res[-1].append(nums[i])
                    j+=1
                else:
                    return []
            elif j==2:
                if nums[i]-nums[i-1]<=k and nums[i]-nums[i-2]<=k:
                    res[-1].append(nums[i])
                    j+=1
                else:
                    return []
            else:
                res.append([nums[i]])
                j=1
        return res
                
                    
            
                
                
            
        
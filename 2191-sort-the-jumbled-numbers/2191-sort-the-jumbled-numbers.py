class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        i=0
        while i<n:
            y=0
            for j in str(nums[i]):
                y+=y*10+mapping[int(j)]
            res[i]=y
            i+=1
        res=list(zip(nums,res))
        res.sort(key=lambda x:x[1])
        return [i for i,j in res]
        
                    
                
            
        
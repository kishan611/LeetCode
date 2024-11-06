class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        temp=[]
        currc=bin(nums[0]).count("1")
        curr=[nums[0]]
        for i in nums[1::]:
            x = bin(i).count("1")
            if x==currc:
                curr.append(i)
            else:
                temp.append(curr)
                curr=[i]
                currc=x
        temp.append(curr)
        prevmx=max(temp[0])
        for i in temp[1::]:
            cmx=max(i)
            cmn=min(i)
            if not prevmx<=cmn:
                return False
            prevmx=cmx
        return True
            
                
        
            
        
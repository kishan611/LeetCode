class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def helper(mid):
            rem=m-1
            lim=position[0]+mid
            for i in position[1::]:
                if i>=lim:
                    lim=i+mid
                    rem-=1
            return rem<=0
        position.sort()
        if m==2:
            return position[-1]-position[0]
        l=1
        h=(position[-1]-position[0])//(m-1)
        while l<h:
            mid=l+(h-l+1)//2
            if helper(mid):
                l=mid
            else:
                h=mid-1
        return l
            
        
                
        
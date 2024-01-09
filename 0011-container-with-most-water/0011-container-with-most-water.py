class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans,l,r=0,0,len(height)-1
        while l<r:
            if height[l]<=height[r]:
                res=height[l]*(r-l)
                i=l+1
                while i<r and height[l]>=height[i]:
                    i+=1
                l=i
            else:
                res=height[r]*(r-l)
                i=r-1
                while i>l and height[r]>=height[i]:
                    i-=1
                r=i
            if res>ans:ans=res
        return ans
        
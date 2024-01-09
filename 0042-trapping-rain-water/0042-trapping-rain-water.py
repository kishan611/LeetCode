class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        water=0
        lm=[0]*n
        rm=[0]*n
        lm[0]=height[0]
        rm[n-1]=height[n-1]
        for i in range(1,n):
            lm[i]=max(height[i],lm[i-1])
        for i in range(n-2,-1,-1):
            rm[i]=max(height[i],rm[i+1])
        for i in range(n):
            water+=min(lm[i],rm[i])-height[i]
        return water
        
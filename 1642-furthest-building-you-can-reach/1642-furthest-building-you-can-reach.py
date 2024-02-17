class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        return self.bs(-1,len(heights),bricks,ladders,heights)
        
    def pt(self,mid,bricks,ladders,heights):
        hd=sorted([heights[i]-heights[i-1] for i in range(1,mid+1) if heights[i]-heights[i-1]>0])
        for d in hd:
            if bricks-d>=0:
                bricks-=d
            elif ladders>0:
                ladders-=1
            else:
                return False
        return True
        
    def bs(self,left,right,bricks,ladders,heights):
        while left+1<right:
            mid=(left+right)//2
            left=mid if self.pt(mid,bricks,ladders,heights) else left
            right=mid if not self.pt(mid,bricks,ladders,heights) else right
        return left
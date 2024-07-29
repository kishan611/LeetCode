import bisect
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sorted_rating=sorted(rating)
        l=[]
        ans=0
        n=len(rating)
        low={}
        for i,v in enumerate(sorted_rating):
            low[v]=i
        for i,v in enumerate(rating):
            x=bisect.bisect(l,v)
            l.insert(x,v)
            diff=low[v]-x
            ans+=x*(n-1-i-diff)+diff*(i-x)
        return ans
            
        
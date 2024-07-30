class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans=count=0
        for a in s:
            if a=='b':
                count+=1
            elif count:
                count-=1
                ans+=1
        return ans
class Solution:
    def maxDepth(self, s: str) -> int:
        maxcount=0
        count=0
        for i in s:
            if i=="(":
                count+=1
                maxcount=max(maxcount,count)
            elif i==')':
                count-=1
        return maxcount
        
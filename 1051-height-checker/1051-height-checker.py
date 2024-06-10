class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        i=0
        count=0
        for j in sorted(heights):
            if heights[i]!=j:
                count+=1
            i+=1
        return count
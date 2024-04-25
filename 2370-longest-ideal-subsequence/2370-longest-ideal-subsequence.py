class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        l=[0]*27
        for c in s[::-1]:
            i=ord(c)-97
            maxi=float('-inf')
            for j in range(max(i-k,0),min(i+k,26)+1):
                maxi=max(l[j],maxi)
            l[i]=maxi+1
        return max(l)
                
                
        
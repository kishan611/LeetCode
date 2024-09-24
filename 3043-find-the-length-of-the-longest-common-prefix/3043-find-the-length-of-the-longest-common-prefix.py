class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s=set()
        for i in arr1:
            x=i
            while x:
                s.add(x)
                x//=10
        length=0
        for i in arr2:
            x=i
            while x and x not in s:
                x//=10
            length=max(0 if x==0 else len(str(x)),length)
        return length
            
        
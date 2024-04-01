class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        count=0
        for i in s[::-1]:
            if c and i==" ":
                break
            if i==" ":
                continue
            else:
                count+=1
                c=1
        return count
                
            
        
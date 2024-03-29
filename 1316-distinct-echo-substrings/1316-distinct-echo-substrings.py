class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        s=set()
        for i in range(1,len(text)//2+1):
            r=i
            count=0
            for l in range(len(text)-i):
                if text[l]==text[r]:
                    count+=1
                else:
                    count=0
                if count==i:
                    s.add(text[l-i+1:l+1])
                    count-=1
                r+=1
        return len(s)
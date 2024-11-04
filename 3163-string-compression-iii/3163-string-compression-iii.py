class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        c,count=word[0],1
        for i in word[1::]:
            if i!=c or count==9:
                comp+=str(count)+c
                c=i
                count=1
            else:
                count+=1
        comp+=str(count)+c
        return comp
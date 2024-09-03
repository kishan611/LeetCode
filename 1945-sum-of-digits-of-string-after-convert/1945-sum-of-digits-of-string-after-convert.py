class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res=""
        for i in s:
            res+=str(ord(i)-96)
        fin=0
        while k>0:
            fin=0
            for i in res:
                fin+=int(i)
            res=str(fin)
            k-=1
        return fin

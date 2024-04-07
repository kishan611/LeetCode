class Solution:
    def checkValidString(self, s: str) -> bool:
        lmax=lmin=0
        for i in s:
            if i=="(":
                lmin+=1
                lmax+=1
            elif i==")":
                lmin-=1
                lmax-=1
            else:
                lmin-=1
                lmax+=1
            if lmax<0:
                return False
            if lmin<0:
                lmin=0
        if lmin==0:
            return True
        return False
        
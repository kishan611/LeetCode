import re
import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        l=re.findall('[+-]?\d+',expression)
        i=0
        resn,resd=0,1
        while i<len(l):
            num,den=int(l[i]),int(l[i+1])
            resn=num*resd+resn*den
            resd*=den
            i+=2
        gcd=math.gcd(resn,resd)
        return f"{resn//gcd}/{resd//gcd}"
            
        
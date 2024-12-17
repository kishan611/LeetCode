class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        def get_i(x,count):
            while x>=0 and not count[x]:
                x-=1
            return x
        res=""
        count=[0]*26
        for i in s:
            count[ord(i)-97]+=1
        i=get_i(25,count)
        j=get_i(i-1,count)
        temp=0
        while i>=0 and j>=0:
            res+=chr(97+i)*min(repeatLimit-temp,count[i])
            res+=chr(97+j)
            count[i]-=min(repeatLimit-temp,count[i])
            temp=0
            count[j]-=1
            if count[i]==0 and count[j]==0:
                i=get_i(j-1,count)
                j=get_i(i-1,count)
            elif count[i]==0:
                i=j
                j=get_i(j-1,count)
                temp=1
            elif count[j]==0:
                j=get_i(j-1,count)
        if i>=0:
            res+=chr(97+i)*min(repeatLimit-temp,count[i])
        return res
            
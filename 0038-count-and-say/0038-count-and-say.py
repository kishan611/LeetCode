class Solution:
    def countAndSay(self, n: int) -> str:
        res="1"
        for i in range(n-1):
            l=len(res)
            c=1
            a=res[0]
            x=""
            for j in range(1,l):
                if res[j]==a:
                    c+=1
                else:
                    x+=str(c)+res[j-1]
                    c=1
                    a=res[j]
            else:
                x+=str(c)+res[-1]
            res=x
        return res
                
        
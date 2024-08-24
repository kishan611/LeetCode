class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def genpan(lh,even):
            pan=lh
            if not even:
                lh//=10
            while lh>0:
                pan=pan*10+lh%10
                lh//=10
            return pan
        num=int(n)
        if num<=10:
            return str(num-1)
        if num==11:
            return '9'
        length=len(n)
        e=(length%2==0)
        lh=int(n[:(length+1)//2])
        possiblepan=[genpan(lh-1,e),genpan(lh,e),genpan(lh+1,e),10**(length-1)-1,10**length+1]
        res=0
        mindiff=float("inf")
        for i in possiblepan:
            if i==num:
                continue
            currdiff=abs(i-num)
            if currdiff<mindiff or (currdiff==mindiff and res>i):
                res=i
                mindiff=currdiff
        return str(res)

        
        
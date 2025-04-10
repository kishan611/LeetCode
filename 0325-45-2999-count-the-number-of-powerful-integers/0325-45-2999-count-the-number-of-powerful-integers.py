class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def helper(num, suf,limit):
            prel = len(num)-len(suf)
            if prel<0:
                return 0
            if prel==0:
                return 1 if num>=suf else 0
            res = 0
            for i in range(prel):
                d = int(num[i])
                if d>limit:
                    res+=(limit+1)**(prel-i)
                    return res
                res+=d*(limit+1)**(prel-i-1)
            if num[-len(suf):]>=suf:
                res+=1
            return res
        return helper(str(finish),s,limit)-helper(str(start-1),s,limit)

        
        
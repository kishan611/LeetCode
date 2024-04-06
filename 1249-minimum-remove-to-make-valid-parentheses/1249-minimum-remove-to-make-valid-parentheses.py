class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        q=[]
        s=list(s)
        n=len(s)
        i=0
        while i<n:
            if s[i]==")":
                if q:
                    q.pop()
                else:
                    s.pop(i)
                    n-=1
                    continue
            elif s[i]=="(":
                q.append(i)
            i+=1
        while q:
            s.pop(q.pop())
        return "".join(s)
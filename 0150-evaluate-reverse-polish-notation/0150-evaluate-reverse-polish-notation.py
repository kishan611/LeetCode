class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        ans=-1
        for i in tokens:
            if i=="+":
                ans=int(s.pop())+int(s.pop())
                s.append(ans)
            elif i=="*":
                ans=int(s.pop())*int(s.pop())
                s.append(ans)
            elif i=="-" or i=='/':
                a=int(s.pop())
                b=int(s.pop())
                if i=='-':
                    s.append(b-a)
                else:
                    c=b//a
                    if c<0 and b%a!=0:
                        s.append(c+1)
                    else:
                        s.append(c)
            else:
                s.append(i)
        return int(s[0])
                
        
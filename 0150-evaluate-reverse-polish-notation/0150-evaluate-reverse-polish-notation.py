class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        ans=-1
        for i in tokens:
            if i=="+":
                s.append(s.pop()+s.pop())
            elif i=="*":
                s.append(s.pop()*s.pop())
            elif i=="-" or i=='/':
                a=s.pop()
                b=s.pop()
                if i=='-':
                    s.append(b-a)
                else:
                    s.append(int(b/a))
            else:
                s.append(int(i))
        return s[0]
                
        
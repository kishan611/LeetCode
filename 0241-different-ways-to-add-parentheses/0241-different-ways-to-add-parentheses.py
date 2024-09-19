class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res=[]
        for i in range(len(expression)):
            o=expression[i]
            if o in "+-*":
                s1=expression[0:i]
                s2=expression[i+1:]
                r1=self.diffWaysToCompute(s1)
                r2=self.diffWaysToCompute(s2)
                for j in r1:
                    for k in r2:
                        if o=="*":
                            res.append(int(j)*int(k))
                        elif o=="+":
                            res.append(int(j)+int(k))
                        elif o=="-":
                            res.append(int(j)-int(k))
        if len(res)==0:
            res.append(int(expression))
        return res
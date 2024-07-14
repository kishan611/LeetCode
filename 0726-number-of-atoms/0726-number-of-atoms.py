class Solution:
    def countOfAtoms(self, formula: str) -> str:
        s=[]
        d={}
        c=""
        num=""
        n=len(formula)
        i=0
        while i<n:
            if not s:
                if formula[i].islower():
                    c+=formula[i]
                elif formula[i].isdigit():
                    while i<n and formula[i].isdigit():
                        num+=formula[i]
                        i+=1
                    i-=1
                    d[c]=d.get(c,0)+int(num)
                    c=""
                    num=""
                elif formula[i].isupper():
                    if c:
                        d[c]=d.get(c,0)+1
                    c=formula[i]
                else:
                    if c:
                        d[c]=d.get(c,0)+1
                        c=""
                    s.append(formula[i])
            else:
                if formula[i].islower():
                    c+=formula[i]
                elif formula[i].isdigit():
                    while i<n and formula[i].isdigit():
                        num+=formula[i]
                        i+=1
                    i-=1
                    s.append([c,int(num)])
                    c=""
                    num=""
                elif formula[i].isupper():
                    if c:
                        s.append([c,1])
                    c=formula[i]
                else:
                    if formula[i]=="(":
                        if c:
                            s.append([c,1])
                            c=""
                        s.append(formula[i])
                    else:
                        if c:
                            s.append([c,1])
                            c=""
                        if i+1<n and formula[i+1].isdigit():
                            i+=1
                            while i<n and formula[i].isdigit():
                                num+=formula[i]
                                i+=1
                            i-=1
                            s2=[]
                            while s[-1]!="(":
                                x=s.pop()
                                x[1]*=int(num)
                                s2.append(x)
                            s.pop()
                            num=""
                            if s:
                                while s2:
                                    s.append(s2.pop())
                            else:
                                while s2:
                                    x=s2.pop()
                                    d[x[0]]=d.get(x[0],0)+x[1]
                        else:
                            s2=[]
                            while s[-1]!="(":
                                s2.append(s.pop())
                            s.pop()
                            if s:
                                while s2:
                                    s.append(s2.pop())
                            else:
                                while s2:
                                    x=s2.pop()
                                    d[x[0]]=d.get(x[0],0)+x[1]
            i+=1
        if c:
            d[c]=d.get(c,0)+1
        res=""
        for i,j in sorted(d.items()):
            if j>1:
                res+=i+str(j)
            else:
                res+=i
        return res



        
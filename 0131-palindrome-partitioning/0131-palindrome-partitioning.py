class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(i,path):
            if i==len(s):
                res.append(path)
                return 
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    backtrack(j,path+[s[i:j]])
        res=[]
        backtrack(0,[])
        return res
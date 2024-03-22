class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            x=list(i)
            x.sort()
            s="".join(x)
            if s in d:
                d[s].append(i)
            else:
                d[s]=[i]
        return d.values()
        
            
        
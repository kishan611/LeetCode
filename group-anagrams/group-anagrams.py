class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            s=sorted(i)
            s="".join(s)
            if s in d:
                d[s].append(i)
            else:
                d[s]=[i]
        return d.values()
        
            
        
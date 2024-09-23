class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n=len(s)
        words=defaultdict(list)
        for i in dictionary:
            words[i[0]].append(i)
        res=[0]*(n+1)
        for i in range(n-1,-1,-1):
            res[i]=res[i+1]+1
            if s[i] in words:
                for word in words[s[i]]:
                    if s[i:i+len(word)]==word:
                        res[i] = min(res[i], res[i + len(word)])
        return res[0]
                    
                    
                    
        
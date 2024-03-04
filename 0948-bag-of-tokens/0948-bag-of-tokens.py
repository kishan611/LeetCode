class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i=0
        j=len(tokens)-1
        maxs=0
        score=0
        while i<=j:
            if tokens[i]>power and score>0:
                power+=tokens[j]
                j-=1
                score-=1
            elif tokens[i]<=power:
                power-=tokens[i]
                score+=1
                maxs=max(maxs,score)
                i+=1
            else:
                return 0
                
        return maxs
        
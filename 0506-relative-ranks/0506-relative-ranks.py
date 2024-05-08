class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score=enumerate(score)
        score=sorted(score,key=lambda x:x[1],reverse=True)
        res=[""]*len(score)
        try:
            res[score[0][0]]="Gold Medal"
            res[score[1][0]]="Silver Medal"
            res[score[2][0]]="Bronze Medal"
        except:
            return res
        x=4
        for i,j in score[3::]:
            res[i]+=str(x)
            x+=1
        return res
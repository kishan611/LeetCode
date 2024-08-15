class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in text:
            if i in d:
                d[i]+=1
        return min(min(d.values()),min(d['l'],d['o'])//2)
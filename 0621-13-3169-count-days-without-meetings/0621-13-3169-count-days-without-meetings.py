class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res = 0
        meetings.sort()
        s = meetings[0][0]
        e = meetings[0][1]
        for i,j in meetings[1::]:
            if i<=e:
                e = max(e,j)
            else:
                res+=e-s+1
                s = i
                e = j
        res += e-s+1
        return days-res
        
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h=[]
        res=[]
        if a>0:
            heapq.heappush(h,(-a,'a'))
        if b>0:
            heapq.heappush(h,(-b,'b'))
        if c>0:
            heapq.heappush(h,(-c,'c'))
        while h:
            co1,ch1=heapq.heappop(h)
            if len(res)>=2 and res[-1]==ch1 and res[-2]==ch1:
                if not h:
                    break
                co2,ch2=heapq.heappop(h)
                res.append(ch2)
                co2+=1
                if co2<0:
                    heapq.heappush(h,(co2,ch2))
                heapq.heappush(h,(co1,ch1))
            else:
                res.append(ch1)
                co1+=1
                if co1<0:
                    heapq.heappush(h,(co1,ch1))
        return "".join(res)
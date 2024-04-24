class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        count=1
        prev=pairs[0][1]
        for i in pairs[1::]:
            if i[0]>prev:
                count+=1
                prev=i[1]
        return count
            
        
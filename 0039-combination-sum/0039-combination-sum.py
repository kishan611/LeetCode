class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp=[]
        res=[]
        n=len(candidates)
        def helper(idx,target):
            if target==0:
                res.append(temp[:])
                return 
            for i in range(idx,n):
                if candidates[i]>target:
                    continue
                temp.append(candidates[i])
                helper(i,target-candidates[i])
                temp.pop()
        helper(0,target)
        return res
        
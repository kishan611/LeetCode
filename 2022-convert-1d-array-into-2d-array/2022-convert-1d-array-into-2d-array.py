class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length=len(original)
        if m*n!=length:
            return []
        res=[]
        for i in range(0,length,n):
            res.append(original[i:i+n])
        return res
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1=Counter(arr1)
        res=[]
        x=[]
        for i in arr2:
            res+=[i]*arr1[i]
            arr1[i]=0
        for i,j in arr1.items():
            x+=[i]*j
        x.sort()
        return res+x
        
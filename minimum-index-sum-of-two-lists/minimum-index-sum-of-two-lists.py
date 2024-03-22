class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        res=[]
        for i in range(len(list1)):
            d[list1[i]]=[i]
        mins=2001
        for i in range(len(list2)):
            if list2[i] in d:
                d[list2[i]].append(i)
                mins=min(mins,sum(d[list2[i]]))
        for i,j in d.items():
            if len(j)==2 and sum(j)==mins:
                res.append(i)
        return res
            
        
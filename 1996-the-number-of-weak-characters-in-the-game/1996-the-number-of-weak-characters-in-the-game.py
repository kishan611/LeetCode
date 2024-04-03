class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        md=0
        count=0
        for a,d in properties:
            if d<md:
                count+=1
            else:
                md=d
        return count
        
            
        
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s=skill[0]+skill[-1]
        res=skill[0]*skill[-1]
        n=len(skill)//2
        for i in range(1,n):
            if skill[i]+skill[-i-1]!=s:
                return -1
            res+=(skill[i]*skill[-i-1])
        return res
        
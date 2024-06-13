class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d=Counter(moves)
        return d.get("U",0)==d.get("D",0) and d.get("L",0)==d.get("R",0)
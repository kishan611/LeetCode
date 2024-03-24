class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dr={i:[] for i in range(9)}
        dc={j:[] for j in range(9)}
        d9={(i,j):[] for i in range(3) for j in range(3)}
        for i,row in enumerate(board):
            for j,val in enumerate(row):
                if val!=".":
                    if val in dr[i]:
                        return False
                    dr[i].append(val)
                    if val in dc[j]:
                        return False
                    dc[j].append(val)
                    if val in d9[(i//3,j//3)]:
                        return False
                    d9[(i//3,j//3)].append(val)
        return True
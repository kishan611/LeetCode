class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res=[]
        for i,row in enumerate(board):
            for j,val in enumerate(row):
                if val!=".":
                    res+=[(i,val),(val,j),(i//3,j//3,val)]
        return len(res)==len(set(res))
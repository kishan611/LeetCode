class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        length=len(word)
        def findword(i,j,k):
            if k==length:
                return True
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!=word[k]:
                return False
            temp=board[i][j]
            board[i][j]=None
            if findword(i+1,j,k+1) or findword(i,j+1,k+1) or findword(i-1,j,k+1) or findword(i,j-1,k+1):
                return True
            board[i][j]=temp
            return False
        for i in range(m):
            for j in range(n):
                if findword(i,j,0):
                    return True
        return False
                    
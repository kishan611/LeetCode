from math import log
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count=0
        while left!=right:
            left>>=1
            right>>=1
            count+=1
            print(left,right)
        return left<<count
        
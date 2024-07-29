class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_single=0
        sum_double=0
        for i in nums:
            if i<10:
                sum_single+=i
            else:
                sum_double+=i
        return not sum_single==sum_double
        
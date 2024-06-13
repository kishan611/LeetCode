class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        s=0
        x=len(seats)
        for i in range(x):
            s+=abs(seats[i]-students[i])
        return s
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        z=students.count(0)
        o=students.count(1)
        for i in sandwiches:
            if i==1:
                o-=1
            else:
                z-=1
            if z==-1 or o==-1:
                return max(z,o)
        return 0
        
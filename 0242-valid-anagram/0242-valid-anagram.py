class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t=list(t)
        for i in s:
            if i in t:
                t.remove(i)
            else:
                return False
        if t:
            return False
        return True
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uc=set()
        c=set()
        for i in s1.split()+s2.split():
            if i in uc:
                c.add(i)
            else:
                uc.add(i)
        return list(uc-c)
            
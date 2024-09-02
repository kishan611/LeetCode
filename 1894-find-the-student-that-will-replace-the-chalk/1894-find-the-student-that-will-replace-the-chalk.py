class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot=sum(chalk)
        k%=tot
        for i in range(len(chalk)):
            if k<chalk[i]:
                return i
            k-=chalk[i]
        return 0
        
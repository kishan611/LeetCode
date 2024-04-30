class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        c=[0]*1024
        res,m,c[0]=0,0,1
        for letter in word:
            m^=1<<(ord(letter)-97)
            res+=c[m]
            for i in range(10):
                res+=c[m^(1<<i)]
            c[m]+=1
        return res
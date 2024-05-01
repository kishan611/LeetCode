class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i=0
        for _ in range(len(word)):
            if word[i]==ch:
                return word[i::-1]+word[i+1:]
            i+=1
        return word
        
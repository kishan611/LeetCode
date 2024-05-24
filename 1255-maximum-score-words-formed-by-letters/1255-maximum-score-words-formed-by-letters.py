class Solution:
    def subsets(self,words,score,count,letter_count,i,curr_score):
        for j in range(26):
            if letter_count[j]>count[j]:
                return 
        self.res=max(self.res,curr_score)
        for j in range(i,len(words)):
            for ch in words[j]:
                letter_count[ord(ch)-ord('a')]+=1
                curr_score+=score[ord(ch)-ord('a')]
            self.subsets(words,score,count,letter_count,j+1,curr_score)
            for ch in words[j]:
                letter_count[ord(ch)-ord('a')]-=1
                curr_score-=score[ord(ch)-ord('a')]
                
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.res=0
        count=[0]*26
        letter_count=[0]*26
        for ch in letters:
            count[ord(ch)-ord('a')]+=1
        self.subsets(words,score,count,letter_count,0,0)
        return self.res
        
    
            
        
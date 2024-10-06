class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1=sentence1.split()
        sentence2=sentence2.split()
        n1,n2=len(sentence1),len(sentence2)
        if n1>n2:
            sentence1,sentence2=sentence2,sentence1
            n1,n2=n2,n1
        i=0
        while i<n1 and sentence1[i]==sentence2[i]:
            i+=1
        j=0
        while j<n1 and sentence1[-(j+1)]==sentence2[-(j+1)]:
            j+=1
        return (i+j)>=n1
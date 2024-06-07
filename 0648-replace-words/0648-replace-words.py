class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sen=sentence.split()
        for i in range(len(sen)):
            for j in dictionary:
                if sen[i].startswith(j):
                    sen[i]=j if len(sen[i])>len(j) else sen[i]
        return " ".join(sen)
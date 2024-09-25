class Trie:
    def __init__(self):
        self.count=0
        self.child={}
    def add(self,s,i):
        if i:
            self.count+=1
        if i==len(s):
            return 
        if not self.child.get(s[i]):
            self.child[s[i]]=Trie()
        self.child[s[i]].add(s,i+1)
    def traversal(self,s,i):
        if i==len(s):
            return self.count
        return self.count+self.child[s[i]].traversal(s,i+1)
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie=Trie()
        for w in words:
            trie.add(w,0)
        ans=[]
        for w in words:
            ans.append(trie.traversal(w,0))
        return ans
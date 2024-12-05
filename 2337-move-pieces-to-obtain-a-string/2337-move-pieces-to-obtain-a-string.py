class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i=j=0
        n=len(start)
        start+='E'
        target+='E'
        while i<n or j<n:
            while i<n and start[i]=='_': i+=1
            while j<n and target[j]=='_': j+=1
            c=start[i]
            if c!=target[j]: return False
            if c=='L' and i<j: return False
            if c=='R' and i>j: return False
            i+=1
            j+=1
        return True
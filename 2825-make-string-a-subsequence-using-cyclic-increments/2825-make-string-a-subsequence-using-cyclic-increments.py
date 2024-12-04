class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i=j=0
        n1,n2=len(str1),len(str2)
        while i<n1 and j<n2:
            if str1[i]==str2[j] or ord(str1[i])+1==ord(str2[j]) or ord(str1[i])-25==ord(str2[j]):
                i+=1
                j+=1
            else:
                i+=1
        if j==n2:
            return True
        return False
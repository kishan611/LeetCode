class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=[int(i) for i in version1.split(".")]
        v2=[int(i) for i in version2.split('.')]
        m=len(v1)
        n=len(v2)
        if m<n:
            v1+=[0]*(n-m)
        elif m>n:
            v2+=[0]*(m-n)
        for i in range(max(m,n)):
            if v1[i]>v2[i]:
                return 1
            if v1[i]<v2[i]:
                return -1
        return 0
        
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans=[0]*n
        x=1
        for i in range(n):
            ans[i]=x
            if (x*10>n):
                if (x==n):
                    x//=10
                x+=1
                while(x%10==0):
                    x//=10
            else:
                x*=10;          
        return ans
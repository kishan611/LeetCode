class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq=[0]*k
        for i in arr:
            rem=((i%k)+k)%k
            freq[rem]+=1
        if freq[0]%2==0:
            for i in range(1,k//2):
                if freq[i]!=freq[k-i]:
                    return False
            if k%2==0:
                if freq[k//2]%2!=0:
                    return False
            else:
                if k==1:
                    return True
                if freq[k//2]!=freq[k-k//2]:
                    return False
            return True
        return False
                
        
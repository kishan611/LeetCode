class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes=[True]*1001
        primes[0]=primes[1]=False
        for i in range(2,33):
            if primes[i]:
                for j in range(i*i,1001,i):
                    primes[j]=False
        primes=[i for i in range(1001) if primes[i]]
        prev=0
        for i in nums:
            if i<=prev:
                return False
            x=bisect_left(primes,i-prev)-1
            if x!=-1:
                i-=primes[x]
            prev=i
        return True
            
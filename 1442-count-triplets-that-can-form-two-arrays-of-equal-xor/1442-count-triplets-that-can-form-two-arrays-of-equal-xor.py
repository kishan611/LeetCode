class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count=0
        for i in range(len(arr)):
            a=arr[i]
            for j in range(i+1,len(arr)):
                a^=arr[j]
                if a==0:
                    count+=j-i
        return count
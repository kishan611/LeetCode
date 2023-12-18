class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1,min2=10000,10000
        max1,max2=0,0
        count1,count2=0,0
        for i in nums:
            if i>max1:
                max1=i
            if i<min1:
                min1=i
        for i in nums:
            if i==max1:
                count1+=1
                if count1==2:
                    max2=max1
            if i==min1:
                count2+=1
                if count2==2:
                    min2=min1
            if i>max2 and i<max1:
                max2=i
            if i<min2 and i>min1:
                min2=i
            
        return max1*max2-min1*min2
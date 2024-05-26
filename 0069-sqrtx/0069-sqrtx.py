class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start,end=0,x
        while start<=end:
            mid=(start+end)//2
            if mid*mid==x:
                return mid
            if mid*mid<x:
                ans=mid
                start=mid+1
            else:
                end=mid-1
        return end
        
        
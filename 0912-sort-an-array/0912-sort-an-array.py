class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        def conquer(arr,left,right):
            i,j,k = 0,0,0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k]=left[i]
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1
            while i<len(left):
                arr[k] = left[i]
                i+=1
                k+=1

            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1
        
                
        
        def divide(arr):
            n = len(arr)
            if n>1:
                mid = n//2
                left = arr[:mid]
                right = arr[mid:]
                divide(left)
                divide(right)
                conquer(arr,left,right)
        divide(nums)
        return nums
    
                
        
        
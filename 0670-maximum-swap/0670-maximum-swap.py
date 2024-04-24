class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=[int(i) for i in str(num)]
        index={j:i for i,j in enumerate(nums)}
        for i in range(len(nums)):
            for d in range(9,nums[i],-1):
                if d in index and index[d]>i:
                    nums[i],nums[index[d]]=nums[index[d]],nums[i]
                    return int("".join(map(str,nums)))
        return num
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        l, r = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    l[i] = max(1 + l[j], l[i])

        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] < nums[i]:
                    r[i] = max(1 + r[j], r[i])

        ans = 0
        for i in range(1, len(nums) - 1):
            if l[i] != 1 and r[i] != 1:
                ans = max(ans, l[i] + r[i])
        return len(nums)-ans+1
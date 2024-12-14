class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans, cnt, lo = 0, Counter(), -1
        for hi, num in enumerate(nums):
            cnt[num] += 1
            while max(cnt) > min(cnt) + 2:
                lo += 1
                cnt[nums[lo]] -= 1
                if cnt[nums[lo]] == 0:
                    del cnt[nums[lo]]
            ans += hi - lo
        return ans
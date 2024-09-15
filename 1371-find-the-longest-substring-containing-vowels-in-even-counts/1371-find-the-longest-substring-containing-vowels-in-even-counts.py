class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mapy = [-2] * 32
        mapy[0] = -1

        max_len = 0
        res = 0

        for i, char in enumerate(s):
            if char == 'a':
                res ^= 1
            elif char == 'e':
                res ^= 2
            elif char == 'i':
                res ^= 4
            elif char == 'o':
                res ^= 8
            elif char == 'u':
                res ^= 16

            prev = mapy[res]
            if prev == -2:
                mapy[res] = i
            else:
                max_len = max(max_len, i - prev)

        return max_len
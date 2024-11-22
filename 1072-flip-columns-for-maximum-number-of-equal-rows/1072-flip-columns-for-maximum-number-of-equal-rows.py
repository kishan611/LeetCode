class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d= Counter()
        for r in matrix:
            p = tuple(r) if r[0] == 0 else tuple(b ^ 1 for b in r)
            d[p] += 1
        return max(d.values())
        
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mono_inc = []
        for val in arr:
            if mono_inc and val < mono_inc[-1]:
                old_max = mono_inc[-1]
                while mono_inc and val < mono_inc[-1]: 
                    mono_inc.pop()
                mono_inc.append(old_max)
            else:
                mono_inc.append(val)
        return len(mono_inc)
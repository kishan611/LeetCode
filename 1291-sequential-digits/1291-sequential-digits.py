class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a=[]
        for i in range(1,10):
            num=i
            nxt=i+1
            while num<=high and nxt<=9:
                num=num*10+nxt
                if low<=num<=high:
                    a.append(num)
                nxt+=1
        return sorted(a)
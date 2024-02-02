class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a=[]
        x=len(str(low))
        for i in range(1,10):
            num=i
            nxt=i+1
            if 9-num>=x-1:
                while num<=high and nxt<=9:
                    num=num*10+nxt
                    if low<=num<=high:
                        a.append(num)
                    nxt+=1
            else:
                break
        return sorted(a)
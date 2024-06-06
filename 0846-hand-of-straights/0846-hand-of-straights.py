from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        hand=Counter(hand)
        while n>0:
            for i,j in sorted(hand.items()):
                for k in range(i,i+groupSize):
                    if hand.get(k,0)==0:
                        return False
                    hand[k]-=1
                    if hand[k]==0:
                        del hand[k]
                if 1:
                    break
            n-=1
        return True
        
        
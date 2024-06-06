from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        hand=Counter(hand)
        while hand:
            x=min(hand)
            for i in range(x,x+groupSize):
                if not hand.get(i,0):
                    return False
                hand[i]-=1
                if hand[i]==0:
                    del hand[i]
        return True
        
        
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        n=len(asteroids)
        i=0
        while i<n:
            if asteroids[i]>0:
                s.append(asteroids[i])
            else:
                if s and s[-1]>0:
                    x=s.pop()
                    if x>abs(asteroids[i]):
                        s.append(x)
                    elif x<abs(asteroids[i]):
                        continue
                else:
                    s.append(asteroids[i])
            i+=1
        return s
                    
                    
                    
        
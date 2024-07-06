class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        minE=min(enemyEnergies)
        if currentEnergy<minE:
            return 0
        points=1
        currentEnergy+=sum(enemyEnergies)
        currentEnergy-=2*minE
        points+=currentEnergy//minE
        return points

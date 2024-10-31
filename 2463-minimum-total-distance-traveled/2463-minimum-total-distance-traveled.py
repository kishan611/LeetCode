class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        fs = []
        for pos, rep in factory:
            for _ in range(rep):
                fs.append(pos)
        ns = len(robot)
        nfs = len(fs)

        dp0 = [0] * (nfs + 1)
        
        dp1 = dp0.copy()
        dp1[nfs] = 1_000_000_000_000_000

        for robot_index in range(ns - 1, -1, -1):
            for factory_slot_i in range(nfs - 1, -1, -1):
                take = abs(fs[factory_slot_i] - robot[robot_index]) + dp0[factory_slot_i + 1]
                skip = dp1[factory_slot_i + 1]
                dp1[factory_slot_i] = min(take, skip)
            dp0, dp1 = dp1, dp0
            dp1[nfs] = 1_000_000_000_000_000
        
        return dp0[0]
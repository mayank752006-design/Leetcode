class Solution(object):
    def nearestDrone(self, drones, target):
        """
        :type drones: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        minimum = float('inf')
        ans = -1
        for i in range(len(drones)):
            val = (abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1]))
            if  val <= drones[i][2]:
                if val < minimum:
                    minimum = val
                    ans = i 


        return ans
                
        
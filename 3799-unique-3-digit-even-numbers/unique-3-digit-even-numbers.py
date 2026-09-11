class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        count = [0]*10

        for num in digits:
            count[num] += 1

        ans = 0

        for last in [0,2,4,6,8]:
            if count[last] == 0:
                continue
            
            count[last] -= 1

            for first in range(1,10):
                if count[first] == 0:
                    continue
                
                count[first] -= 1

                ans += sum(1 for x in range(10) if count[x] > 0)
                
                count[first] += 1

            count[last] += 1
        
        
        return ans   
class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        min_odd = float('inf')
        
        # for finding minimum odd
        for num in nums1:
            if num % 2 != 0:
                min_odd = min(min_odd, num)

        for num in nums1:
            if num % 2 == 0 and min_odd != float('inf'):
                if num < min_odd:
                    return False
        return True
        
        
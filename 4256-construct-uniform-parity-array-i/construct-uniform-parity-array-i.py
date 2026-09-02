class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        
        n = len(nums1)
        nums2 = [0]*n
        
        #even
        for i in range(n):
            if nums1[i] % 2 == 0:
                nums2[i] = nums1[i]
            else:
                j = 0
                while j < n:
                    if j == i:
                        j += 1
                        continue

                    num = nums1[i] - nums1[j]

                    if num % 2 == 0:
                        nums2[i] = num
                    j += 1
        result = True
        for ch in nums2:
            if ch % 2 != 0:
                result = False

        if (result):
            return True
        
        nums2 = [0]*n

        for i in range(n):
            if nums1[i] % 2 != 0:
                nums2[i] = nums1[i]
            else:
                j = 0
                while j < n:
                    if i == j:
                        j += 1
                        continue
                    
                    num = nums1[i] - nums1[j]
                    if num % 2 != 0:
                        nums2[i] = num
                    j += 1
        
        result = True

        for ch in nums2:
            if ch % 2 == 0:
                result = False

        return result
            
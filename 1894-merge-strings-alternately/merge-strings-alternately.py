class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        i = 0 
        j = 0
        
        while i < len(word1) and j < len(word2):
            res += word1[i]
            i += 1
            res += word2[j]
            j+= 1

        while i < len(word1):
            res += word1[i]
            i += 1

        while j < len(word2):
            res += word2[j]
            j += 1

        return res
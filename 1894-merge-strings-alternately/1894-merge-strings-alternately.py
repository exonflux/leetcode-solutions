class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1list = list(word1)
        word2list = list(word2)
        
        merged = ""
        
        limit = min(len(word1), len(word2))

        for i in range(limit):
            merged += word1list[i] + word2list[i]

        merged += "".join(word1list[limit:])
        merged += "".join(word2list[limit:])

        return merged
        
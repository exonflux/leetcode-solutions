class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        List1 = list(s)
        List2 = list(t)
        
        List1.sort()
        List2.sort()


        for i in range(len(s)):
            if List1[i] != List2[i]:
               return List2[i]

        return List2[-1]
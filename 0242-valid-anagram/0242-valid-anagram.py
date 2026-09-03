class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = list(s)
        T = list(t)

        S.sort()
        T.sort()

        if len(T) != len(S):
            return False

        for i in range(len(T)):
            if S[i] != T[i]:
                return False
        return True

        
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hay = list(haystack)
        needlestack = list(needle)
        
        for i in range (len(hay) - len(needlestack) + 1):
            if hay[i] == needlestack[0]:
                match = True
                for j in range(1,len(needlestack)):
                    if hay[j+i] != needlestack[j]:
                        match = False
                        break
                if match:
                    return i
        return -1
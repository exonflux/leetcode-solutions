class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)
        
        if n == 1:
            return False
            
        length = 1
        while length <= n // 2:
            
            if n % length == 0:
                substring = ""
                for i in range(length):
                    substring += s[i]
                    
                built_string = ""
                multiplier = n // length
                
                for count in range(multiplier):
                    for char in substring:
                        built_string += char
                        
                if built_string == s:
                    return True
                    
            length += 1
            
        return False
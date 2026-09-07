class Solution(object):
    def plusOne(self, digits):

        num_str = "".join(str(d) for d in digits)

        new_str = str(int(num_str) +1)

        return [int(char) for char in new_str]
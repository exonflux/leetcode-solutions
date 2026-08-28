class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        # Basicly get the string look for a odd number to use as a middle char
        #split all chars in half so i can build left side  and reverse it to right and left + mid + right
        #if that doesnt work backtrack to building left side and look for a greater char to implement


        LengthS = len(s)
        counts = Counter(s)
        
        Odd_chars = []
        for char, count in counts.items():
            if count % 2 == 1:
                 Odd_chars.append(char)
        if len(Odd_chars) > 1:
            return ""

        if len(Odd_chars) > 0:
            middle = Odd_chars[0]
        else:
            middle = ""

        half = []
        for char, count in counts.items():
            half.extend([char] * (count // 2))
        half.sort()
        L = LengthS // 2

        available = Counter(half)
        match = 0

        for i in range(L):
            current_char = target[i]

            if available[current_char] > 0:
                available[current_char] -= 1
                match +=1
            else:
                break

        if match == L:
            left = target[:L]
            reversed_left  = left[::-1]
            answer = left + middle + reversed_left

            if answer > target:
                return answer


        index = match if match < L else L - 1
        available = Counter(half)
        for i in range(index):
            available[target[i]] -= 1
        
        for i in range(index, -1, -1):
            current_target = target[i]

            valid = []
            for char, count in available.items():
                 if count > 0 and char > current_target:
                    valid.append(char)

            if len(valid) > 0:
                chosen_char = min(valid)
                available[chosen_char] -=1

                leftovers = []
                for char, count in available.items():
                    leftovers.extend([char] * count)
                leftovers.sort()


                final_left = target[:i] + chosen_char + "".join(leftovers)

                return final_left + middle + final_left[::-1]

            if i > 0:
                available[target[i-1]] += 1

        return ""
                    


        

        
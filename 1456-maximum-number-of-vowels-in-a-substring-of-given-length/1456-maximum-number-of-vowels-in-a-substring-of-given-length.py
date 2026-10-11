class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_vowel = 0  
        window_sum = 0     
        vowel = "aeiou"
        for i in range(k):
            if s[i] in vowel:
                window_sum +=1
        max_vowel = window_sum

        for j in range(k , len(s)):
            if s[j -k] in vowel :
                window_sum -=1

            if s[j] in vowel :
                window_sum +=1

            max_vowel = max(window_sum , max_vowel)
        return max_vowel
        




              

    



            



        
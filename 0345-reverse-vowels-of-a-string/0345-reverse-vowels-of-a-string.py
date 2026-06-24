class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            if s[left].lower() in  "aeiou" and s[right].lower() in   "aeiou":
                s[left] , s[right] = s[right] ,s[left]
                left +=1
                right -=1
            elif s[left].lower() not in  "aeiou":
                left +=1
                continue
            else:
                right -=1
        return "".join(s)

            
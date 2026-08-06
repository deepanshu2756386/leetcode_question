class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        reverse_word = ""
        for i in s+" ":
            if i !=" ":
                result = i+result
            else:
                reverse_word = reverse_word +" "+result
                result = ""

        return reverse_word.strip()
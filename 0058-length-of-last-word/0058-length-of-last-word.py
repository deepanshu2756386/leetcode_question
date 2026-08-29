class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_space = False
        result = ""
        for char in s.strip():
            if not char.isspace():
                result = result + char
                prev_space = False
            else:
                if prev_space == False:
                    result = result + " " 
                    prev_space = True 
        res = ""
        for ch in range(len(result)-1,-1,-1):
            if result[ch] != " ":
                res = res+result[ch]
            else:
               return  len(res)

        return len(res)

            
        
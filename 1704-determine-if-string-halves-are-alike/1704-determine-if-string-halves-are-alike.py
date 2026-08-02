class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mid = len(s)//2
        count1 = 0   
        for i in s[mid:].lower():
            if  i in ["a","e","i","o","u"]:
                count1 +=1 
           

        count2 = 0
        for j in s[0:mid].lower():
            if  j  in ["a","e","i","o","u"]:
                count2 +=1

        if count1 == count2:
            return True
        else:
            return False
        
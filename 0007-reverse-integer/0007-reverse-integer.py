class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign =-1 if x<0 else 1
        
        x = abs(x)
        
    
        result = 0
        while x>0:
            remainder = x%10 
            result =result*10+remainder
            x = x//10
        total =sign*result
        if total <-2**+31 or total > 2**31-1:
            return 0
        return total
    
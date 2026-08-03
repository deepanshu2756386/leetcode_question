class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(s)< len(p):
            return []

        p_count =dict()
        window_count = dict()

        for ch in p:
            if ch not in p_count :
                p_count[ch] = 1
            else:
                p_count[ch] +=1

        left = 0
        result = []

        for  right in range(len(s)):
            if s[right] in window_count:
                window_count[s[right]] +=1

            else:
                window_count[s[right]] = 1

            
            if right - left +1 > len(p):
                window_count[s[left]] -= 1

                if window_count[s[left]] == 0: 
                    del window_count[s[left]] 

                left +=1

            if window_count == p_count:
                result.append(left)

        return result





        
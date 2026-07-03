class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        freq = dict()
        left = 0
        max_len =  0
        for right  in range(len(fruits)) :
            if fruits[right] not in freq :
                freq[fruits[right]] = 1
            else:
                freq[fruits[right]] += 1

            while len(freq) > 2 :
                left_item = fruits[left] 
                freq[left_item] -=1

                if freq[left_item] == 0:
                    del freq[left_item] 
                left +=1
            max_len = max(max_len , right-left+1)

        return max_len

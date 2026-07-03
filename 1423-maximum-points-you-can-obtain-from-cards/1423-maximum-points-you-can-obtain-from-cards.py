class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(cardPoints) ==  k:
            return sum(cardPoints[:k])

        current_card = sum(cardPoints[:k])
        max_card = current_card 

        for i in range(1,k+1):
            current_card = current_card - cardPoints[k-i]
            current_card = current_card + cardPoints[-i]
            max_card = max(max_card,current_card)


        return max_card
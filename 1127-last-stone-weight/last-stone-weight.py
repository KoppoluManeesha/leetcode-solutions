class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
            stones.sort()
            x=stones.pop()
            y=stones.pop()
            if y!=x:
                stones.append(x-y)
        return stones[0] if stones else 0
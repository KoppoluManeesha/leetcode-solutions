class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        spaces=text.count(" ")
        words=text.split()
        n=len(words)
        if n==1:
            return words[0]+" "*spaces
        words_spaces = spaces/(n-1)
        end_space = spaces%(n-1)
        return (" "*words_spaces).join(words)+" "*end_space
        
            


                
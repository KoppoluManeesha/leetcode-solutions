class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num=-1
        for item in s.split():
            if item.isdigit():
                prev=int(item)
                if prev<=num:
                    return False
                num=prev

        return True

                
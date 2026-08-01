class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest_pal={}
        for ch in s:
            longest_pal[ch]=longest_pal.get(ch,0)+1
        length=0
        for count in longest_pal.values():
            length+=(count//2)*2
            if length%2==0 and count%2==1:
                length+=1
        return length

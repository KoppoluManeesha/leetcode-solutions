class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations=set()
        for word in words:
            morse_word=""
            for ch in word:
                index=ord(ch)-ord('a')
                morse_word+=morse[index]
            transformations.add(morse_word)
        return len(transformations)

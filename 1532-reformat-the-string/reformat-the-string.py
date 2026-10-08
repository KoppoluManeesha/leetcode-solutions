class Solution:
    def reformat(self, s: str) -> str:
        digits=[]
        letters=[]
        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letters.append(ch)
        diff=len(digits)-len(letters)
        if abs(diff)>1:
            return ''
        result=''
        if len(letters)>=len(digits):
            for i in range(len(digits)):
                result+=letters[i]
                result+=digits[i]
            if len(letters)>len(digits):
                result+=letters[-1]
        else:
            for i in range(len(letters)):
                result+=digits[i]
                result+=letters[i]
            if len(digits)>len(letters):
                result+=digits[-1]
        
        return result

                    
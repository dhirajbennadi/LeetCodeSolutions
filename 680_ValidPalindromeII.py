class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        
        #Two Pointer
        while left < right:
            if s[left] != s[right]:
                #Inclusion of last index is tricky
                #Remove one character and check if the string is still palindrome
                skipL = s[left+1:right+1]
                skipR = s[left:right]
                
                #Checking with string is palindrome by reversing
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            left += 1
            right -= 1
        
        return True
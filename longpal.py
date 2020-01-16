class Solution:
    def longestPalindrome(self, s: str) -> str:
      
        def isPalindrome(string):
            """return True if palindrome""" 
            # first check if the whole word is a palindrome
            if len(s) % 2 == 0: # if even number
                midpt = len(s)//2

            elif len(s) % 2 != 0: # if odd number
                midpt = len(s)//2 - 1

            if s[:midpt] == s[midpt:]:
                return True
            else:
                return False

        

        
        # if word is NOT a palindrome traverse string
        
        pal = '' # build palindrome
        seen = [] # store letters that have already been reviewed
        longest = '' # holds the longest palindrome
        
        # traverse ltr in string
            # add ltr to pal
            # append ltr to seen
            # if len pal > 1
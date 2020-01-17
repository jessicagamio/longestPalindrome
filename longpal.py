
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
    sub = ''
    seen = '' # store letters that have already been reviewed
    longest = '' # holds the longest palindrome
    
    # traverse ltr in string
        
        # if seenis empty
            # add ltr to sub 
            # add ltr to seen
        # else
            # iterated seen_ltr through seen[::-1]
                # sub equals ltr plus seen_ltr
                # if sub isPalindrome:
                    # compare lenof longest with len of sub
                    # if len(sub) is longer than len(longest)
                        # make longest = sub

        # return longest

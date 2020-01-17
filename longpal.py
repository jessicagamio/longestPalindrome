import unittest

def isPalindrome(s):
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


def longestPalindrome(s):
  
    # if word is NOT a palindrome traverse string
    substring = ''
    seen = '' # store letters that have already been reviewed
    longest = '' # holds the longest palindrome
    
    # traverse ltr in string
    for ltr in s:  
        if seen == '': # if seenis empty
            seen = ltr# add ltr to seen
        else: # else
            for seen_ltr in seen[::-1]:# iterated seen_ltr through seen[::-1]
                substring = ltr + seen_ltr # sub equals ltr plus seen_ltr
                
                if isPalindrome(substring):# if sub isPalindrome:
                    # compare lenof longest with len of sub
                    if len(substring) > len(longest):# if len(sub) is longer than len(longest)
                        longest = substring# make longest = sub

    # return longest
    return longest


class TestFunction(unittest.TestCase):
    def testLongestPalindrome(self):
        self.assertEqual(longestPalindrome('babad'),'bab')


if __name__=="__main__":
    unittest.main()
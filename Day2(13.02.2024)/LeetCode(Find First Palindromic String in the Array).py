Find First Palindromic String in the Array : 

Solution:

class Solution(object):
    def firstPalindrome(self, words):
        for i in words:
            if i==i[::-1]:
                return i

        return ""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            temp = x
            tot = 0
            while temp!=0:
                rem = temp%10
                tot = tot*10+rem
                temp//=10
            return True if tot==x else False

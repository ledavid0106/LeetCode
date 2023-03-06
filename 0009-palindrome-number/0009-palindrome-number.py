class Solution(object):
    def isPalindrome(self, x):
        if x<0:
                return False

        inputNum = x
        newNum = 0
        while x>0:
            newNum = newNum * 10 + x%10
            x = x//10
        return newNum == inputNum
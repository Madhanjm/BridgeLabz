"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=s.lower()
        s2=""
        for i in s1:
            if(i>='a'and i<='z') or (i>='0'and i<='9'):
                s2+=i

        rev=""
        i=0
        for _ in s2:
           i+=1 
        while i>0:
            rev+=s2[i-1]
            i-=1
        if s2==rev:
            return True
        else:
            return False
        

s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))

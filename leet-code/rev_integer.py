"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
       
        if x<0:
            rev_num="-"+str(abs(x))[::-1]
        else:
            rev_num=str(abs(x))[::-1]
        rev_num=int(rev_num)
        if rev_num<=(2**31)-1 and rev_num>=-2**31 :
            return int(rev_num)
    
        return 0
x=int(input())
sol=Solution()
print(sol.reverse(x))
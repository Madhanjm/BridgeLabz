"""
412. Fizz Buzz
Solved
Easy
Topics
premium lock icon
Companies
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list=[]
        for i in range(n):
            if (i+1)%3==0 and (i+1)%5==0:
                list.append("FizzBuzz")
            elif (i+1)%5==0:
                list.append("Buzz")
            elif (i+1)%3==0:
                list.append("Fizz")
            else:
                
                list.append(str(i+1))
        return list
        
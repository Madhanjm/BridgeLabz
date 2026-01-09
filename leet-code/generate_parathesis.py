"""22. Generate Parentheses
Solved
Medium
Topics
premium lock icon
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        def backtrack(current,open,close):
            if len(current)==n*2:
                result.append(current)
                return 
            if open<n:
                backtrack(current+"(",open+1,close)

            if close<open:
                backtrack(current+")",open,close+1)

        backtrack("",0,0)
        return result

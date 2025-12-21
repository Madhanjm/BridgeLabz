"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs=="":
            return ""
        prefix=strs[0]

        for word in strs[1:]:
            i=0
            while i<len(prefix) and i<len(word) and prefix[i]==word[i]:
                i+=1
            prefix=prefix[:i]
            if prefix=="":
                return ""
        return prefix
        
strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))
"""
https://leetcode.com/problems/assign-cookies/description/

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with;
 and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. 
 Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]
Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: [1,2], [1,2,3]
Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Approach #1, greedy
        #
        # the problem description is vague, but according to the test result, it means
        # * the cookies are different kinds of cookies
        # * one kind of cookies can only be allocated to one child, once allocated, cannot split to other child
        # * one child can only take one kind of cookie
        # a single loop can 
        #
        # sort two lists
        # try to satisfy all less-greedy child with cookies of less number
        # If sj >= gi, content_child +1
        # if the sj<gi, try next kind of cookie (j++)
        #
        # O(nlogn) for sorting, 46%
        
        g.sort()
        s.sort()
        i,j = 0,0
        while j < len(s) and i<len(g):
            if s[j] >= g[i]: i+=1
            j+=1
        return i


if __name__ == '__main__':
    s = Solution()
    tc = [([1,2,3], [1,1]),([1,2], [1,2,3]),([1,2,3], [3])]
    an = [1,2,2]
    for i in range(len(tc)):
        print(s.findContentChildren(tc[i][0],tc[i][1]))
        #assert(s.findContentChildren(tc[i][0],tc[i][1]) == an[i])

"""
https://leetcode.com/problems/reverse-string-ii/description/

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]


"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Approach #1, naive
        #
        # reverse necessary and combine together
        #
        # "abcdefg", k=2
        # [abcd] [efg]
        # [ab][cd] [ef][g]
        # [ba][cd] [fe][g]
        # divmod(7,2*2) = (1,3)
        # [0:2]           [2:4]         [4:6][6:]
        # [2*0:2*(0+1)]   [2*1:2*(1+1)] ...
        #
        # O(n) 99%
        d,m = divmod(len(s),k)
        ans = ""
        reverse = True
        for i in range(d):
            b = k*i
            ans = ans + s[b:b+k][::-1] if reverse else ans + s[b:b+k]
            reverse = not reverse
        ans = ans + s[d*k:][::-1] if reverse else ans + s[d*k:]
        return ans
        
        
if __name__ == '__main__':
    s = Solution()
    tc  = [("abcdefg",2),("abcdefgh",3)]
    ans = ["bacdfeg","cbadefhg"]
    
    for i in range(len(tc)):
        r = s.reverseStr(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])

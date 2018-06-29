"""
https://leetcode.com/problems/number-of-lines-to-write-string/description/

We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units,
and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths,
an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line?
Return your answer as an integer list of length 2.



Example :
Input:
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
Output: [3, 60]

Explanation:
All letters have the same length of 10. To write all 26 letters,
we need two full lines and one line with 60 units.

Example :
Input:
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
Output: [2, 4]

Explanation:
All letters except 'a' have the same length of 10, and
"bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
For the last 'a', it is written on the second line because
there is only 2 units left in the first line.
So the answer is 2 lines, plus 4 units in the second line.


Note:

The length of S will be in the range [1, 1000].
S will only contain lowercase letters.
widths is an array of length 26.
widths[i] will be in the range of [2, 10].
"""
xrange = range
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        # Approach #1, map
        #
        # map alphabet to int
        # accumulate until > 100
        #
        # O(n), 99%
        lines = 1
        count = 0
        for c in S:
            c_len = widths[ord(c)-97] # ord('a') = 97
            count += c_len
            if count >100:
                lines +=1
                count = c_len
        return [lines, count]


if __name__ == '__main__':
    s = Solution()
    tc =  [ ([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"), \
            ([ 4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa") ]
    ans = [ [3, 60], [2, 4] ]
    for i in range(len(tc)):
        r = s.numberOfLines(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])

""" 
https://leetcode.com/problems/count-and-say/description/
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # solution 1: Divide and conqure, recursive, countAndSay(n) = countAndSay( int(countAndSay(n-1)) )
        # 1: 1 -> 11
        # 2: 11 -> 21
        # 3: 21-> 1211
        # 4: 1211-> 111221
        # 5: 111221
        # 6: 312211
        # 7: 13112221
        # 8: 1113213211
        # 9: 31131211131221
        #10: 13211311123113112211
        # time O(n^2), 98%, 40ms
        
        # memorization, lookup table for n <10

        list = [0, 1, 11, 21, 1211, 111221 , 312211, 13112221, 1113213211, 31131211131221, 13211311123113112211]
        if(n<=10): return str(list[n])

        r = list[10]

        # refactor and improve efficiency
        # skip int/str conversion
        # input r, outpu r -> input s, output s
        s=str(r)
        for i in range(10, n):
            start  = 0
            next   = 1
            count  = 1
            result = ''
            length = len(s)
            while (start < length and next < length):
                if s[next] == s[start]:
                    count+=1
                    next +=1
                else:
                    result = result + str(count) + s[start]
                    count = 1
                    start = next
                    next +=1
            s = result + str(count) + s[start]

        return s

        

d = Solution()
#print(d.countAndSay(3))

for i in range(1,11):
    print(d.countAndSay(i))

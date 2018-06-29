"""
https://leetcode.com/problems/letter-case-permutation/description/

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.

"""
xrange = range
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # Approach #2, itertools.product
        #
        # TODO:
        # fit the purpose of itertools.product
        #  . generate the input for itertools.product()
        #  . create the answer
        #
        # example
        #  "a1b2", the input should be ['a','A'],'1',['b','B'],'2'
        #
        # O(n), 51%
        s = []
        for c in S:
            if c.isalpha():
                s.append([c.lower(), c.upper()])
            else:
                s.append(c)
        
        ans = []
        import itertools
        for i in list(itertools.product(*s)):
            ans.append("".join(i))
        return ans

        exit()
        # Approach #1, binary digits, brute-force
        #
        # for n letters in S, there are 2^n elements
        # 0: lower
        # 1: upper
        #
        # . save letters' index in a list letters, n = len(letters)
        # . enumerate from 0 ~ (2^n-1)
        # . upper(1s' bits)
        #
        # O(2^n), 10%
        S = S.lower()
        letters = []
        for i,c in enumerate(S):
            if c.isalpha(): letters.append(i)
        ans = []
        for j in xrange(pow(2,len(letters))):
            s = list(S)
            map = bin(j)[2:].zfill(len(letters))
            for upper, idx in zip(map,letters):
                if upper == '1': s[idx] = s[idx].upper()
            ans.append("".join(s))
        return ans





if __name__ == '__main__':
    s = Solution()
    tc =  [ "a1b2", "3z4", "12345" ]
    ans = [ ["a1b2", "a1B2", "A1b2", "A1B2"],  ["3z4", "3Z4"],["12345"] ]
    for i in range(len(tc)):
        r = s.letterCasePermutation(tc[i])
        print (r)
        assert(r == ans[i])

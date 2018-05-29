"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
class Solution(object):
    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Approach #1, naive
        # use Counter for p
        # traverse s and looking for same Counter
        # if use Counter with every index of s
        # O(m*n) or O(n^2)
        # if use a dict for s, keep updating, O
        # 
        # Time Limit Exceeded
        # 
        from collections import Counter
        #cp = Counter(p)
        size = len(p)
        ans = []
        for i in range(len(s)- size +1):
            c = Counter(s[i:size+i])-Counter(p)
            if len(list(c.elements())) == 0:
                ans.append(i)
        return ans
        
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Approach #2, reuse answer #242
        # use dict to keep both p and sliding window s
        # 
        # O(n),  72%
        #
        ans = []
        size = len(p)
        pd = {}
        for c in p:
            if c in pd:
                pd[c]+=1
            else:
                pd[c]=1
        sd = {}
        for c in s[:size]:
            if c in sd:
                sd[c]+=1
            else:
                sd[c]=1
        for i in range(len(s)- size +1):
            if pd == sd: ans.append(i)
            #print(pd,sd,i)
            sd[s[i:i+1]] -=1
            if sd[s[i:i+1]] == 0: del sd[s[i:i+1]]
            sd[s[i+size:i+size+1]] = sd.get(s[i+size:i+size+1],0) + 1

        return ans
        

if __name__ == '__main__':
    s = Solution()
    tc = [("cbaebabacd","abc"),("abab","ab"),("","p")]
    #tc = [("cbaebabacd","abc")]
    an = [[0, 6],[0, 1, 2],[]]
    for t in tc:
        print(s.findAnagrams(t[0],t[1] ))

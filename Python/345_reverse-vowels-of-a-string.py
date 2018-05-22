"""
https://leetcode.com/problems/reverse-vowels-of-a-string/description/


Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach #1, 
        # find index of all vowels
        # switch characters based on index
        # O(n), 96%
        vowels = set('aeiouAEIOU')
        v = []
        for i,e in enumerate(s):
            if e in vowels: v.append(i)
        last = len(v)

        s2 = list(s)
        #print(s2)
        for i in range((last)//2):
            a = v[i]
            b = v[last-i-1]
            tmp = s2[a]
            s2[a] = s2[b]
            s2[b] = tmp
        return "".join(s2)
        

if __name__ == '__main__':
    tc = ["hello","leetcode","Aa","aA"]
    ans = ["holle", "leotcede"]
    s = Solution()
    for t in tc:
        print(s.reverseVowels(t))



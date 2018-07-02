"""
https://leetcode.com/problems/goat-latin/description/

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
 

Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.

"""
xrange = range
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Approach #1, naive
        #
        # str.split() to list
        # if s[0] not in set {a, e, i, o, u}, s = s[1:]+s[0]
        # postfix "ma"  is common
        # postfix "a*"  is based on index
        #
        # O(n), 37ms
        words = S.split()
        vowels = set("aeiouAEIOU")
        for i, word in enumerate(words):
            if word[0] not in vowels:
                words[i] = word[1:]+word[0]
            words[i] = "".join([words[i], "ma", "a"*(i+1)])
            
        return " ".join(words)
        


if __name__ == '__main__':
    s = Solution()
    tc =  [  "I speak Goat Latin", "The quick brown fox jumped over the lazy dog" ]
    ans = [ "Imaa peaksmaaa oatGmaaaa atinLmaaaaa", "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa" ]
    for i in range(len(tc)):
        r = s.toGoatLatin(tc[i])
        print (r)
        assert(r == ans[i])

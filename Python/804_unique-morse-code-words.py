"""
https://leetcode.com/problems/unique-morse-code-words/description/

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-",
(which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".


Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""
xrange = range
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Approach #1, brute-force
        #
        # transform all words into Morse Code string
        # add transformed strings to a set s
        # return len(s)
        #
        # O(n), 42%
        #
        alphabets = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        def morse(c):
            return alphabets[ord(c)-ord('a')]
        s = set()
        for word in words:
            s.add("".join( map(morse,list(word))))

        return len(s)






if __name__ == '__main__':
    s = Solution()
    tc =  [ ["gin", "zen", "gig", "msg"] ]
    ans = [ 2 ]
    for i in range(len(tc)):
        r = s.uniqueMorseRepresentations(tc[i])
        print (r)
        assert(r == ans[i])

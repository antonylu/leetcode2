"""
http://www.cnblogs.com/grandyang/p/5187041.html

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Approach #0, brute-force
        # find all positions of word1 in a list
        # find all positions of word2 in b list
        # find min of all elements in a and b where abs(a-b) is smallest
        # O(2n+a*b)
        w1 = []
        w2 = []
        for i,w in enumerate(words):
            if   w == word1: w1.append(i)
            elif w == word2: w2.append(i)
        #print(w1,w2)
        ans = len(words)
        for i in w1:
            for j in w2:
                ans = min(ans, abs(i-j))
        return ans



if __name__ == "__main__":
    tc = ["practice", "makes", "perfect", "coding", "makes"]
    a  = ("coding","practice")
    b  = ("makes", "coding" )
    s = Solution()
    
    print(s.shortestDistance(tc,a[0],a[1]))
    print(s.shortestDistance(tc,b[0],b[1]))

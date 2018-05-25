"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # approach #3, the string contain only lowercase letters.
        # look for all lowercase letters
        # s.find, s.rfind
        #
        # 40ms, 100%
        lowercases = "abcdefghijklmnopqrstuvwxyz"
        ans = len(s)
        for c in lowercases:
            left = s.find(c)
            if left != -1:
                right = s.rfind(c)
                if right == left:
                    #print(left)
                    ans = min(ans,left)
        return ans if ans < len(s) else -1

        # approach #2, use dict to save first occurences 
        # count then find without conversion, sould be faster
        # O(n), 50%
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] +=1
            else:
                dict[s[i]] = 1
        
        for i in range(len(s)):
            if dict[s[i]] == 1: return i
        return -1
        

        # approach #1, use Counter
        # O(n) 29%
        from collections import Counter
        c = Counter(s)
        d = dict(c)
        for i in range(len(s)):
            if d[s[i]] == 1: return i
        return -1
        
        
        
                

if __name__ == '__main__':
    tc = ["leetcode", "loveleetcode","aabbccddeeffgghhijkllkji","aadadaad"]
    #tc = ["loveleetcode"]
    ans = [0,2,-1,-1]
    s = Solution()
    for (i) in tc:
        #s.firstUniqChar(i)
        print(s.firstUniqChar(i))



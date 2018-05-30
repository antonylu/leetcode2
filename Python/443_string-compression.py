"""
https://leetcode.com/problems/string-compression/description/

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Approach #1, naive with 3 references
        # ref1 to current char
        # ref2 to check if == ref1,
        # if same, count +=1
        # if not same:
        #    if count >1: append char number after ref1
        #    reset count, ref1 = ref2
        # Space O(1)
        # Time O(n), 91%
        r1 = 0
        count = 0
        cur = 0
        for r2 in range(len(chars)):
            if chars[r2] == chars[r1]:
                count +=1
            else:
                chars[cur] = chars[r1]
                cur +=1
                if count >1:
                    s = str(count)
                    count = 1
                    for i in range(len(s)):
                        chars[cur] = s[i:i+1]
                        cur +=1
                r1 = r2
        chars[cur] = chars[r1]
        cur +=1
        if count >1:
            s = str(count)
            count = 1
            for i in range(len(s)):
                chars[cur] = s[i:i+1]
                cur +=1
        #print(chars)
        return cur
                
                    

if __name__ == '__main__':
    s = Solution()
    tc = [["a","a","b","b","c","c","c"],["a"],["a","b","b","b","b","b","b","b","b","b","b","b","b"]]
    #tc = [["a","a","b","b","c","c","c"]]
    an = [6,1,4]
    for i in range(len(tc)):
        print(s.compress(tc[i]))
        #assert(s.compress(tc[i]) == an[i])

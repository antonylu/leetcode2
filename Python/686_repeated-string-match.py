"""
https://leetcode.com/problems/repeated-string-match/description/

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # Approach #2, ceil(len(B)/len(A)) or +1 is the possible answer
        # the ceil can be written as -(-len(B)//len(A))
        #
        # O(n), 100% 33ms, this is the 4th time get 100%
        #
        if len(set(B) - set(A)) >0: return -1

        repeat = -(-len(B)//len(A))
        AA = A*repeat
        if B in AA: return repeat
        AA = "".join([AA,A])
        if B in AA: return repeat+1

        return -1


        # Approach #1, naive
        # 1. repeat A until len(A+) <= len(B)
        # 2. compare and repeat A until len(A+) > 4* len(B)

        # Approach #1a, brute force
        # repeat A and compare and repeat A until len(A+) > 3 x len(B)
        # use set to exclude obvious invalid test case
        # O(n), 95%
        if len(set(B) - set(A)) >0: return -1

        AA = A
        repeat = 1
        while repeat == 1 or len(AA) < 3* len(B):
            if B in AA: return repeat
            AA = "".join([AA,A])
            repeat +=1
        return -1

        # Approach #1, brute force
        # repeat A and compare and repeat A until len(A+) > 3 x len(B)
        #
        # O(n), 4.9%
        AA = A
        repeat = 1
        while repeat == 1 or len(AA) < 3* len(B):
            if B in AA: return repeat
            AA = "".join([AA,A])
            repeat +=1
        #print(AA,B)
        return -1


if __name__ == '__main__':
    s = Solution()
    tc  = [ ("abcd","cdabcdab"),("aaaa","a"),("abababaaba","aabaaba")]
    ans = [ 3,1,2]

    for i in range(len(tc)):
        r = s.repeatedStringMatch(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])

"""
https://leetcode.com/problems/self-dividing-numbers/description/

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
The boundaries of each input argument are 1 <= left <= right <= 10000.

"""
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Approach #1a, brute-force
        # with str()
        #
        # check every number between left and right
        # O(n), 68%
        def isSelfDriving(n):
            for d in str(n):
                if d == '0' or n%int(d) !=0 : return False
            return True
        ans = []
        for i in range(left, right+1):
            if isSelfDriving(i): ans.append(i)
        return ans

        # Approach #1, brute-force
        # with divmod()
        #
        # check every number between left and right
        # O(n), 80%
        def isSelfDriving(n):
            # refactoring
            d = n
            while d > 0:
                d,m = divmod(d,10)
                if m == 0 or n % m != 0: return False
            return True

            """
            d,m = divmod(n,10)
            while d > 0:
                #print(n,d,m)
                if m == 0 or n % m != 0: return False
                d,m = divmod(d,10)
            if m == 0 or n % m != 0: return False
            return True
            """


        ans = []
        for i in range(left, right+1):
            if isSelfDriving(i): ans.append(i)
        return ans




if __name__ == '__main__':
    s = Solution()
    tc =  [ (1,22) ]
    ans = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]]

    for i in range(len(tc)):
        r = s.selfDividingNumbers(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])

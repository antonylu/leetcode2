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
        # Approach #2, lookup table with binary search
        #
        # O(1), 100%
        # although binary search is O(log n), n is limited, so it is O(1)
        #
        sdn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99, 111, 112, 115, 122, 124, 126, 128, 132, 135, 144, 155, 162, 168, 175, 184, 212, 216, 222, 224, 244, 248, 264, 288, 312, 315, 324, 333, 336, 366, 384, 396, 412, 424, 432, 444, 448, 488, 515, 555, 612, 624, 636, 648, 666, 672, 728, 735, 777, 784, 816, 824, 848, 864, 888, 936, 999, 1111, 1112, 1113, 1115, 1116, 1122, 1124, 1128, 1131, 1144, 1155, 1164, 1176, 1184, 1197, 1212, 1222, 1224, 1236, 1244, 1248, 1266, 1288, 1296, 1311, 1326, 1332, 1335, 1344, 1362, 1368, 1395, 1412, 1416, 1424, 1444, 1448, 1464, 1488, 1515, 1555, 1575, 1626, 1632, 1644, 1662, 1692, 1715, 1722, 1764, 1771, 1824, 1848, 1888, 1926, 1935, 1944, 1962, 2112, 2122, 2124, 2128, 2136, 2144, 2166, 2184, 2196, 2212, 2222, 2224, 2226, 2232, 2244, 2248, 2262, 2288, 2316, 2322, 2328, 2364, 2412, 2424, 2436, 2444, 2448, 2488, 2616, 2622, 2664, 2688, 2744, 2772, 2824, 2832, 2848, 2888, 2916, 3111, 3126, 3132, 3135, 3144, 3162, 3168, 3171, 3195, 3216, 3222, 3264, 3276, 3288, 3312, 3315, 3324, 3333, 3336, 3339, 3366, 3384, 3393, 3432, 3444, 3492, 3555, 3612, 3624, 3636, 3648, 3666, 3717, 3816, 3864, 3888, 3915, 3924, 3933, 3996, 4112, 4116, 4124, 4128, 4144, 4164, 4172, 4184, 4212, 4224, 4236, 4244, 4248, 4288, 4332, 4344, 4368, 4392, 4412, 4416, 4424, 4444, 4448, 4464, 4488, 4632, 4644, 4824, 4848, 4872, 4888, 4896, 4932, 4968, 5115, 5155, 5355, 5515, 5535, 5555, 5775, 6126, 6132, 6144, 6162, 6168, 6192, 6216, 6222, 6264, 6288, 6312, 6324, 6336, 6366, 6384, 6432, 6444, 6612, 6624, 6636, 6648, 6666, 6696, 6762, 6816, 6864, 6888, 6912, 6966, 6984, 7112, 7119, 7175, 7224, 7266, 7371, 7448, 7476, 7644, 7728, 7777, 7784, 8112, 8128, 8136, 8144, 8184, 8224, 8232, 8248, 8288, 8328, 8424, 8448, 8488, 8496, 8616, 8664, 8688, 8736, 8824, 8832, 8848, 8888, 8928, 9126, 9135, 9144, 9162, 9216, 9288, 9315, 9324, 9333, 9396, 9432, 9612, 9648, 9666, 9864, 9936, 9999]
        from bisect import bisect_left
        from bisect import bisect_right
        return sdn[bisect_left(sdn,left):bisect_right(sdn,right)]

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
    tc =  [ (1,22),(47,85) ]
    ans = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22], [48,55,66,77]]

    for i in range(len(tc)):
        r = s.selfDividingNumbers(tc[i][0],tc[i][1])
        print (r)
        assert(r == ans[i])

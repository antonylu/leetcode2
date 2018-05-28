"""
https://leetcode.com/problems/binary-watch/description/

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # Approach #1, brute-force
        # enumerate all possible combination 0~11: 0~59
        # append the time to a list which index is the number of On LED
        #
        # Python 3, 92%
        # Python 2, 81%
        ans = [[] for x in range(10)]
        for h in range(0,12):
            for m in range(0,60):
                bits = bin(h).count('1') + bin(m).count('1')
                if bits == num:
                    ans[bits-1].append( "{:d}:{:0>2d}".format(h,m))
        return ans[num-1]

        # Approach #2, combinations
        # use itertools for combination
        # enumerate all possible combination for n LED on, 
        # 10 LEDS, get a list of itertools.combinations(10,n), 
        # for each combination, check valid (0~11:0~59)
        # append the time to a list which index is the number of On LED
        # 

        # Approach #3, look up table
        # there are only 10 LEDs
        # make a list[10], with all the answers (12 x 60 = 720 items)
        # O(1), should be the fastest 100%

if __name__ == '__main__':
    s = Solution()
    for i in range(1,11):
        print(s.readBinaryWatch(i))
    #print(s.readBinaryWatch(1))

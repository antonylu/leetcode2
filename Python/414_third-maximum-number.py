"""
https://leetcode.com/problems/third-maximum-number/description/

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach #2, 
        # use set() to remove duplicates
        # use sort()
        # O(n) or O(n log n), 94%
        s = list(set(nums))
        s.sort(reverse=True)
        return s[2] if len(s)>2 else s[0] 
        

        # Approach #1, naive
        # evaluate each value and keep the 3 max
        # O(n), 33%
        m1 = nums[0]
        m2, m3 = None, None
        for i in nums[1:]:
            if i > m1:
                m3 = m2
                m2 = m1
                m1 = i
            elif i == m1:continue
            else:
                if not m2: 
                    m2 = i
                    continue
                elif i > m2:
                    m3 = m2
                    m2 = i
                elif i == m2:continue
                else:
                    if not m3:
                        m3 = i
                        continue
                    elif i == m3:continue
                    elif i > m3:
                        m3 = i
        #print(m1,m2,m3)
        return m3 if m3 != None else m1
            
        
if __name__ == '__main__':
    s = Solution()
    tc = [[3, 2, 1],[1, 2],[2, 2, 3, 1],[1],[3,3,3],[3,3,4,3,4,3,0,3,3]]
    ans = [1,2,1,1,3,0]
    for t in tc:
        print(s.thirdMax(t))

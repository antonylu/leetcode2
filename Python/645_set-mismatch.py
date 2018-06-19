"""
https://leetcode.com/problems/set-mismatch/description/

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

"""
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach #2, set operation
        # Counter to find duplicate
        # most_common for duplicate
        # search 0 for missing
        # O(n), 4.34%
        from collections import Counter
        c = Counter(nums)
        dup = c.most_common(1)[0][0]
        
        for i in range(1,len(nums)+1):
            if c[i] == 0: 
                missing = i
                break
        return [dup, missing]

        # Approach #1, set operation
        # create a correct set
        # subset to get the missing number
        # Counter
        # the one with 2
        #
        # O(n), 15%
        from collections import Counter
        c = Counter(nums)
        dup = c.most_common(1)[0][0]
        
        missing = list(set([i for i in range(1,len(nums)+1)]) - set(nums))[0]
        return [dup, missing]
        


if __name__ == '__main__':
    s = Solution()
    tc  = [ [1,2,2,4]]
    ans = [ [2,3] ]
    for i in range(len(tc)):
        r = s.findErrorNums(tc[i])
        print (r)
        assert(r == ans[i])

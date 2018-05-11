"""
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## Approach #1 brute force, Incremental, enumeration, two nested loops
        ## space O(1)
        ## time  O(n^2), beats 4%, 6637ms
        #  
        #for i in range(0, len(numbers)-1) :
        #    for j in range(i+1, len(numbers)):
        #        if (target == numbers[i]+numbers[j] ):
        #            return [i,j]

        # Approach #4
        # improve Approach #2 by using enumerate
        # memorization, hash table, put (target - numbers[i]) in dict
        # if it exists then both found. One-pass hash table
        # hash table look up average = O(1)
        # 
        # space O(n)
        # time  O(n), 23%, 49 ms
        d = {}
        for i, n in enumerate(numbers):
            s = target - n
            if s in d:
                return [d[s] + 1, i+1]
            d[n] = i

        # Approach #2, binary search sorted list for O(N logN)
        # min,max,mid
        # 85ms, 5%
        for i in range(0, len(numbers)-1) :
            search = target - numbers[i]
            min = i+1
            max = len(numbers) -1 
            while min <= max:
                mid = (min+max)//2
                if (search == numbers[mid]):
                    return [i+1,mid+1]
                if search > numbers[mid]:
                    min = mid +1
                else:
                    max = mid -1

        
        # Approach #3
        # no2. memorization, hash table, put (target - numbers[i]) in dict
        # if it exists then both found. One-pass hash table
        # hash table look up average = O(1)
        # space O(n)
        # time  O(n), 22%, 50 ms
        d = {}
        for i in range(0, len(numbers)):
            if (numbers[i] in d.keys() ): 
                return [d[numbers[i]]+1,i+1]
            else:
                d[(target- numbers[i])] = i

if __name__ == "__main__":
    s=Solution()
    n = [2,7,11,15]
    t = 9
    print(s.twoSum(n,t))

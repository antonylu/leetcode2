"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Approach #2, since there are n elements in the list, use the minus/positive as False/True flag in each element
        # kind of thining out of box
        # when getting value, use abs()
        # Time O(n), 6%
        # Space O(1)
        # traverse the list, for number i, mark nums[i] as negative
        # traverse 1~n, if nums[i] is Positive, append it to the answer
        ans = []
        for i in nums:
            i=abs(i)
            nums[i-1] = abs(nums[i-1])* -1
        for j in range(len(nums)):
            if nums[j] > 0:
                ans.append(j+1)
        return ans
        

        # Approach #1, brute-force naive
        # create a list with full integers
        # remove element from the list according to input nums
        # space O(n)
        # time  O(n)

        # Approach #1a, brute-force naive
        # create a set with full integers
        # substract the set of nums
        # space O(n)
        # time  O(n) 13%
        s1 = set(nums)
        s2 = set(range(1,len(nums)+1))
        return list(s2-s1)

        # Approach #2, sort the list in-place
        # count and compare the list, record the missing
        # space O(1)
        # time  O(nlog n)
        #
        print(nums)
        nums.sort()
        c = 1
        i = 0
        ans = []
        print(nums)
        while c <= len(nums):
            if c != nums[i]:
                ans.append(c)
                i+=1
            else:
                i+=1
                c+=1
            
        return ans
        

if __name__ == '__main__':
    s = Solution()
    tc = [[4,3,2,7,8,2,3,1],[]]
    an = [5,6]
    for i in range(len(tc)):
        print(s.findDisappearedNumbers(tc[i]))
        #assert(s.findDisappearedNumbers(tc[i]) == an[i])

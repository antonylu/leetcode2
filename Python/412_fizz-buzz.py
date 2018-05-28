"""
https://leetcode.com/problems/fizz-buzz/description/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

"""
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Approach #1, naive
        #
        # 87%
        ans = []
        for i in range(1,n+1):
            c = ""
            if i % 3 == 0 and i % 5 == 0: 
                ans.append("FizzBuzz")
            elif i % 3 == 0: 
                ans.append("Fizz")
            elif i % 5 == 0: 
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
        
            
        
if __name__ == '__main__':
    s = Solution()
    tc = [15,12]
    for t in tc:
        print(s.fizzBuzz(t))

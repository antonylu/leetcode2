"""
https://leetcode.com/problems/count-primes/description/


Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution(object):
    # Approach #1, brute force
    # a prime number can only be divided cleanly by 1 and itself
    # i.e., for all 1< x <n, n%x !=0
    # O(n^2),  Time Limit Exceeded
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(2,n):
            ans += self.isPrime(i)
        return ans
    def isPrime(n):
        for x in range(2,n):
            if n%x == 0: return 0
        return 1

    # Approach #2, Eratosthenes
    # a prime number can only be divided cleanly by 1 and itself
    # i.e., for all 1< x <n, n%x !=0
    # try 2~sqrt(n)
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # O(NlogNlogN)
    # 1019ms, 48%
    def countPrimes(self, n):
        a = 0
        temp = [1] * (n)
        for i in range(2, n):
            if (temp[i]):
                j = i * i
                while (j <= n-1):
                    temp[j] = 0
                    j = j + i
                    
        for i in range(2, n):
            if (temp[i]):
                a+=1
        return a

if __name__ == "__main__":
    s = Solution()
    tc  = [10,12,0,2,499979]
    ans = [4,5,0,0,41537]
    for t in tc:
        print(s.countPrimes(t))


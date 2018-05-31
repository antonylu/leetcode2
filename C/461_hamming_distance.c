/*
// https://leetcode.com/problems/hamming-distance/description/
// 
// The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
// 
// Given two integers x and y, calculate the Hamming distance.
// 
// Note:
// 0 ≤ x, y < 231.
// 
// Example:
// 
// Input: x = 1, y = 4
// 
// Output: 2
// 
// Explanation:
// 1   (0 0 0 1)
// 4   (0 1 0 0)
//        ↑   ↑
//
// The above arrows point to positions where the corresponding bits are different.
//
*/
#include <stdio.h>

int hammingDistance(int x, int y) {
    int h = 0 ;
    int z = x ^ y;
    
    while(z)
    {
        z &= (z-1);
        h++;
    }
    
    return h;
}

void main(void)
{
    int res = 0;
    res = hammingDistance(2,4);
    printf("%d\n", res);
}


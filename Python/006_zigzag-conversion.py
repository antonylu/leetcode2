"""
https://leetcode.com/problems/remove-linked-list-elements/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Approach #1, direct, use list[numRows] to save all substring
        # the string are distributed as "running suicide" with inversed direction (+1/-1)
        # join the string and return
        # O(n), 71% 113ms
        size = len(s)
        if numRows == 1 or size <= numRows:
            return s

        dir  = 1
        boxN = 0
        box  = [""] * numRows # 0~numRows-1
        for c in s:
            box[boxN] += c
            if boxN == numRows -1: 
                dir = -1
            elif boxN == 0: 
                dir = 1
            boxN += dir
        ans = ''
        for ss in box:
            ans += ss
        return ans
            
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        # Approach #1, brute forice
        # based on rows, 
        if numRows == 1 or len(s) <= numRows:
            return s
        
        index = 0
        numCheck = numRows * 2 - 2        
        tempDict = {}        
        line = numRows - 1
        
        for char in s:
            remainder = index % numCheck
            
            if remainder >= numRows:
                remainder = line - remainder % line
            
            if remainder in tempDict:
                tempDict[remainder] += char
            else:
                tempDict[remainder] = char                
            index += 1
            
        returnStr = ""
        for index in range(numRows):
            returnStr +=  tempDict[index]
        
        return returnStr        

if __name__ == "__main__":
    s=Solution()
    tc = ["PAYPALISHIRING","PAYPALISHIRING"]
    ans = [3,4]
    r = ["PAHNAPLSIIGYIR","PINALSIGYAHRPI"]
    for i in range(len(tc)):
        #print(s.convert(tc[i],ans[i]))
        assert(s.convert(tc[i],ans[i]) == r[i])

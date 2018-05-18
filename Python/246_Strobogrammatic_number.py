"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

"""
class Solution(object):
    def isStrobogrammatic(self, s):
        # Approach #1, compare every number in hash table
        # 
        # 018 and 6 vs 9
        # [609, 818, 1881 690181069]
        dict = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        i = 0
        l = len(s)
        while i < (l +1)//2:
            if s[i] not in dict: return False
            if s[l-1-i] not in dict: return False
            if s[i] != dict[s[l-1-i]]: return False
            i+=1
        return True
        
                
if __name__ == "__main__":
    tc = ["609", '818', "1881", "690181069", "690181069", "2",""]
    s = Solution()
    for t in tc:
        print(s.isStrobogrammatic( t ) )

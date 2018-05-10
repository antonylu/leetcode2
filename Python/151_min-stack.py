""" 
https://leetcode.com/problems/linked-list-cycle/description/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class MinStack(object):
    # Approach #1, use list as stack
    # implement min
    # 997ms, 18%
    stack = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        del self.stack[:]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()  


if __name__ == "__main__":
    minStack = MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    print(minStack.getMin())#;   --> Returns -3.
    minStack.pop();
    print(minStack.top())#;      --> Returns 0.
    print(minStack.getMin())#;   --> Returns -2.
    minStack = MinStack();
    minStack.push(-1);
    print(minStack.top())#;      --> Returns 0.
    print(minStack.getMin())#;   --> Returns -2.
    
    

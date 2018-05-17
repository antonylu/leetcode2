"""
https://leetcode.com/problems/implement-stack-using-queues/description/

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

"""
from collections import deque

class MyStack(object):
    # Approach #1, use collections.deque
    # User the Queue reversely, i.e., keep pop, top and empty the same.
    # But when push, move the entire queue below the pushed item, i.e., pop all items and add in the queue
    # the pop, top, empty: same O(1) as queue
    # push: O(n)
    # 31ms, 80%
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        # 31ms, 80%
        self.queue.rotate(1)

        # 38ms, 20%
        #for i in range(len(self.queue) - 1):
        #    self.queue.append(self.queue.popleft())
            
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.popleft()
        
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0 
        
        

class MyStack2(object):
    # Approach #2, use list for stack
    #
    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """



if __name__ == "__main__":
    # Your MyStack object will be instantiated and called as such:

    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_2)
    print(param_3)
    print(param_4)

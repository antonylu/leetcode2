"""
https://leetcode.com/problems/implement-queue-using-stacks/description/

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""
class MyQueue(object):
    # Approach #1, 
    # suppose pop runs less than push in overall test cases
    # push is the same as stack push
    # pop from left is actually implemented by pop all from right and push back until the last one O(n)
    # 
    # use stack as queue
    # 
    # Queue   |1|2|3 <-- push
    # Stack   |1|2|3 <-- push
    #
    # Queue <-|1|2|3     pop
    # Stack   |1|2|3 --> pop to another stack len()-1 times, pop 3, push back from antoher stack
    #
    # use list.append           as push
    #     list.pop              as pop
    #     list[0]               as peek
    #  
    # pop O(n), others O(1), 29ms, 98%
    
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myqueue = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.myqueue.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        tmp = []
        for i in range(len(self.myqueue)-1):
            tmp.append(self.myqueue.pop())
        tmp.reverse()
        ans = self.myqueue.pop()
        for j in tmp:
            self.myqueue.append(j)
        
        return ans
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.myqueue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.myqueue) == 0
        


# Your MyQueue object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.pop()
    param_4 = obj.pop()
    print(param_2)
    print(param_3)
    print(param_4)

"""
https://leetcode.com/problems/employee-importance/description/
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively.
Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []].
Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11

Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3.
They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.

Note:
One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Approach #2, BFS
        # 1. create a hash dict of ID vs (Importance,[sub]) with Dict comprehension
        #    to speed up the ID lookup O(n)
        # 2. BFS and sum up
        #
        # O(n), 27%
        d = {e.id: (e.importance, e.subordinates) for e in employees}
        self.ans = 0
        from collections import deque
        q = deque([d[id]])
        while len(q) > 0:
            employee = q.popleft()
            self.ans += employee[0]
            for subID in employee[1]:
                q.append(d[subID])

        return self.ans
        # Approach #1a, DFS
        # 1. create a hash dict of ID vs (Importance,[sub]) with Dict comprehension
        #    to speed up the ID lookup O(n)
        # 2. DFS and sum up
        #
        # it's not clear what employees is, after test, it is a list of Employee objects
        #
        # O(n), 42%

        d = {e.id: (e.importance, e.subordinates) for e in employees}
        self.ans = 0
        def dfs(id):
            self.ans += d[id][0]
            for e in d[id][1]:
                dfs(e)

        dfs(id)
        return self.ans

        # Approach #1, DFS
        # 1. create a hash dict of ID vs (Importance,[sub])
        #    to speed up the ID lookup O(n)
        # 2. DFS and sum up
        #
        # it's not clear what employees is, after test, it is a list of Employee objects
        #
        # O(n), 58%

        d = {}
        for e in employees:
            d[e.id] = (e.importance, e.subordinates)

        self.ans = 0
        def dfs(id):
            self.ans += d[id][0]
            for e in d[id][1]:
                dfs(e)

        dfs(id)
        return self.ans



if __name__ == '__main__':
    s = Solution()
    tc  = [ ([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1),([[1,2,[2]], [2,3,[]]],2)]
    ans = [ 11,3 ]


    for i in range(len(tc)):
        employees = []
        for j in tc[i][0]:
            e = Employee(j[0], j[1], j[2])
            employees.append(e)
        r = s.getImportance(employees,tc[i][1])
        print (r)
        #assert(r == ans[i])

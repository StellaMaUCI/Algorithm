import collections


class Solution:
    def __init__(self):
        self.res = []

    def dfs(self, graph, node):
        def rec(node):
            if node in self.res:
                return
            self.res.append(node)
            nxts = []
            for nei in graph[node]:
                if nei not in self.res:
                    nxts.append(nei)
            for nxt in sorted(nxts):
                rec(nxt)

        rec(node)
        return self.res

 #https: // www.geeksforgeeks.org / breadth - first - search - or -bfs -for -a - graph /
    def bfs(self, graph, node):
        self.res.append(node)
        queue = collections.deque([node])
        while queue:
            cur = queue.popleft()
            for nei in sorted(graph[cur]):
                if nei not in self.res:
                    self.res.append(nei)
                    queue.append(nei)
        return self.res


graph = {'A': ['D', 'B', 'I'], 'B': ['A', 'C', 'D', 'E'], 'C': ['B', 'E', 'F'], 'D': ['A', 'B', 'E', 'G'],
         'E': ['B', 'C', 'D', 'F', 'G', 'H'], 'F': ['C', 'E', 'H'], 'G': ['D', 'E', 'H', 'I', 'J'],
         'H': ['E', 'F', 'G', 'J'], 'I': ['A', 'G', 'J'], 'J': ['I', 'G', 'H']}

s = Solution()
print(s.dfs(graph, 'A'))
s1 = Solution()
print(s1.bfs(graph, 'A'))
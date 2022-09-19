#adjacency matrix->adjacency lists->incidence matrix->adjacency lists
import collections
from collections import defaultdict


class Solution:
    def __init__(self):
        self.edgeN = 0
        self.nodeN = 0
        self.nodeI = 0
        self.edge = []



#adjacency matrix->adjacency list O(n^2)
    def adjM_adjL(self, adjM):
        adjL = collections.defaultdict(list) #要生成字典，但没有默认值，使用它生成默认值，而不keyerror
        for i in range(len(adjM)):
            for j in range(len(adjM)):
                if (adjM[i][j]):
                    adjList[i].append(j)
                    adjList[j].append(i)
        return adjList



 # adjacency lists->incidence matrix O(n^2)
    def adjL_incM(self, adjL):
        self.edgeN = sum(len(adj) for adj in adjL.values())
        self.nodeN = len(adjL)
        self.nodeI = collections.defaultdict()
        for i, node in enumerate(adjL):
            self.nodeI[node] = i #extract information from list to node

        self.edges = []
        incM = [[0] * self.edgeN for _ in range(self.nodeN)] #multiple arrays for incidence matrix
        for node in adjL:
            for nei in adjL[node]:
                if {node, nei} not in self.edge:
                    incM[self.nodeI[node]][len(self.edge)] = 1
                    incM[self.nodeI[nei]][len(self.edge)] = 1
                    self.edge.append({node, nei})
        return incM


# incidence matrix->adjacency lists O(n^2)
    def incM_adjL(self, incM):
        adjL = collections.defaultdict(list)
        for j in range(len(incM)):
            a = b = -1
            for i in range(len(incM)):
                if (incM[i][j]):
                    if a == -1:
                        a = i
                    else:
                        b = i
            if b != -1:
                adjL[a].append(b)
                adjL[b].append(a)
        return adjL


def main():
    graph = {'A': ['D', 'B', 'I'], 'B': ['A', 'C', 'D', 'E'], 'C': ['B', 'E', 'F'], 'D': ['A', 'B', 'E', 'G'],
             'E': ['B', 'C', 'D', 'F', 'G', 'H'], 'F': ['C', 'E', 'H'], 'G': ['D', 'E', 'H', 'I', 'J'],
             'H': ['E', 'F', 'G', 'J'], 'I': ['A', 'G', 'J'], 'J': ['I', 'G', 'H']}
    # graph1 = {'A': ['B', 'E'], 'B': ['A', 'F', 'C'], 'C': ['B', 'G', 'D'], 'D': ['C', 'H'], 'E': ['A', 'F', 'I'],
    #           'F': ['B', 'E', 'J', 'G'], 'G': ['C', 'F', 'K', 'H'], 'H': ['D', 'G', 'L'], 'I': ['E', 'J', 'M'],
    #           'J': ['I', 'F', 'K', 'M'], 'K': ['G', 'J', 'L', 'O'], 'L': ['H', 'K', 'P'], 'M': ['I', 'N'],
    #           'N': ['J', 'M', 'O'], 'O': ['N', 'K', 'P'], 'P': ['O', 'L']}

    s = Solution()
    incM = s.adjL_incM(graph)
    for row in incM:
        print(row)
    adjList = s.incM_adjL(incM)
    print(adjList)
    print(s.edges)
    print(s.nodeI)

if __name__ == "__main__":
    main()

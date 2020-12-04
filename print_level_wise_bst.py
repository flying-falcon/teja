class Scanner:
    def __init__(self):
        self.tokens = []
    def next(self):
        while len(self.tokens) == 0:
            self.tokens = input().strip().split()
            self.tokens.reverse()
        return self.tokens.pop()
    def nextint(self):
        return int(self.next())


class Node:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = Node


# Modify the code to traverse a Binary tree
def bfs_visit(node):
    from collections import deque
            
def main():
    sc = Scanner()
    n, m = sc.nextint(), sc.nextint()
    g = [[] for i in range(n)]
    for i in range(m):
        u, v = sc.nextint(), sc.nextint()
        g[u].append(v)
        g[v].append(u)

    distance = [1e9 for i in range(n)]
    pi = [-1 for i in range(n)]
    visited = [False for i in range(n)]
    # alternatively we can avoid use of visited array by using information from distance array
    # for unvisited vertices[u], distance[u] = inf
    for i in range(n):
        if not visited[i]:
            bfs_visit(g, n, m, i, visited, pi, distance)
    
main()

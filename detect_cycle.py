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



# Modify the code to print "No cycle" or "Cycle"
def bfs_visit(g, n, m, root, visited, pi, distance):
    from collections import deque
    q = deque()
    q.append(i)
    visited[i] = True
    distance[i] = 0
    while len(q) != 0:
        u = q.popleft()
        for v in g[u]:
            if not visited[v]:
                visited[u] = True
                distance[v] = min(distance[v], distance[u] + 1)
                pi[v] = u 
            
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


"""Test 1

3 3
0 1
1 2
2 0

Test 2
3 2
0 1
1 2
"""

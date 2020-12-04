# graph representation
# n = number of vertices

def main():
    # code for graph/tree representation
    n = 10, m = 14
    g = [[] for i in range(n)]
    # undirected
    for i in range(m):
        u, v = scan<int, int>()
        g[u].append(v)
        g[v].append(u)
    
    # connected graph bfs
    queue<int> q;
    vector<bool> visited(n)
    vector<int> dist(n, 1e9)
    # fix the root 0
    q.push(0)
    visited[0] = true;
    dist[0] = 0
    while (len(q) != 0):
        int u = q.front()
        q.pop()
        for(v : g[u]) :
            if not visited[v]:
                q.push(v)
                visited[v] = true
                dist[v] = min(dist[v], dist[u] + 1):
    
    # extend to multiple components

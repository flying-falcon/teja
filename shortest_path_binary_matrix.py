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

sc = Scanner()

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def shortest_path(A, n, m, i, j):
    
def main():
    n, m = sc.nextint(), sc.nextint()
    A = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            A[i][j] = sc.nextint()

    shortest_path(A, n, m, i, j)
    
main()

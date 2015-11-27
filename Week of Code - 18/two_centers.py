import sys

N = int(input().strip())
D = [[ [50000, 0][r == c] for r in range(N)] for c in range(N)]

for line in sys.stdin:
    p, c = line.strip().split(' ')
    p, c = [int(p)-1, int(c)-1]
    D[p][c] = 1
    D[c][p] = 1
    
for k in range(N):
    D = [[min(D[r][c], D[r][k] + D[k][c]) for r in range(N)] for c in range(N)]

d_min = 50000
for n1 in range(N):
    for n2 in range(n1+1, N):
        d_max = 0
        for ni in range(N):
            if ni != n1 and ni != n2:
                d = min(D[ni][n1], D[ni][n2])
                d_max = max(d_max, d)
        d_min = min(d_min, d_max)
print(d_min)    
    
    
#    treeNode[p].add(c)
#    treeNode[c].add(p)    
#    parent.add(p)
#    childs.add(c)       
#roots = list(parent-childs) + list(childs - parent)
#print(roots)
#print(int(math.ceil(max([get_max_depth(n, treeNode, set()) for n in roots]) / 4.0)))





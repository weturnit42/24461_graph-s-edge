import copy

N = int(input())
tree = ()
vertex = []
edge = []

for i in range(N):
    vertex.append(i)
for i in range(N-1):
    a, b = map(int, input().split())
    edge.append((a, b))
tree = (vertex, edge)

cnt = []
for i in range(N):
    cnt.append(0)
for k in range(len(tree[1])):
    for i in range(N):
        for j in range(N):
            if(tree[1][k] == (i, j) or tree[1][k] == (j, i)):
                cnt[i] = cnt[i] + 1
                cnt[j] = cnt[j] + 1
for i in range(N):
    cnt[i] = int(cnt[i]/2)

while(True):
    preEdge = copy.deepcopy(edge)
    i=0
    while(i<len(vertex)):
        j=0
        if(cnt[i] == 1):
            while(j<len(edge)):
                if(tree[1][j] == (i, j)):
                    print(i, j)
                    tree[1][j] = (-1, -1)
                    cnt[i] = cnt[i] - 1
                    cnt[j] = cnt[j] - 1
                if(tree[1][j] == (j, i)):
                    print(j, i)
                    tree[1][j] = (-1, -1)
                    cnt[i] = cnt[i] - 1
                    cnt[j] = cnt[j] - 1
                j=j+1
            tree[0][i] = -1
        i=i+1
    if(edge == preEdge):
        break

for i in range(len(vertex)):
    if(vertex[i] != -1):
        print(vertex[i], end=' ')
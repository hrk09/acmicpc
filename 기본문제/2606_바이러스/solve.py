'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7

4
'''
# dfs로 풀기

def dfs(s):
    global cnt
    stack.append(s)
    visited[s] = 1
    for i in range(1, v+1):
        if g[s][i] and not visited[i]:
            cnt += 1
            dfs(i)
    return stack

# 입력값 받기
v = int(input())
e = int(input())
edges = []
visited = [0] * (v+1)
stack = []
cnt = 0

for _ in range(e):
    edges.extend(map(int, input().split()))

g = [[0]*(v+1) for i in range(v+1)]

for i in range(0, len(edges), 2):
    g[edges[i]][edges[i+1]] = 1
    g[edges[i+1]][edges[i]] = 1
dfs(1)

print(cnt)
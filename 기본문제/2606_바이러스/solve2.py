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
# bfs로 풀기
def bfs(s):
    global cnt
    # 시작점을 q에 넣고
    q.append(s)
    # q 가 없을때까지 돌림
    while q:
        # 조사할 거 q에서 하나 뽑음
        n = q.pop(0)
        # 조사할 대상 n이 방문한 적이 없으면,
        if n not in visited:
            # visited 에 n을 하나 추가하고
            visited.append(n)
            # n의 연결노드들을 하나씩 돌면서
            for i in range(v+1):
                # n번째 i 연결노드가 존재하고, visited 한 적없고, q에 없으면,
                if g[n][i] and i not in visited and i not in q:
                    # q에 비로소 i가 들어가고
                    q.append(i)
                    # cnt += 1한다
                    cnt += 1
    return visited

v = int(input())
e = int(input())
edges = []
for _ in range(e):
    edges.extend(map(int, input().split()))
# print(edges)

g = [[0] * (v+1) for i in range(v+1)]
for i in range(0, len(edges), 2):
    g[edges[i]][edges[i+1]] = 1
    g[edges[i+1]][edges[i]] = 1

q = []
visited = []
cnt = 0
bfs(1)
print(cnt)
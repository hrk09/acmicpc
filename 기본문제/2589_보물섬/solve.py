# 최단거리 bfs
'''
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW

8
'''
def is_safe(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True

def bfs(x, y):
    q = []
    q.append((x, y))

    dist = [[0] * M for i in range(N)]
    dist[x][y] = 1
    while q:
        (x, y) = q.pop(0)
        for (dx, dy) in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            nx = x + dx
            ny = y + dy
            if is_safe(nx, ny):
                if gold_map[nx][ny] == 'L' and dist[nx][ny] == 0:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    return max(sum(dist, [])) - 1


N, M = map(int, input().split())
gold_map = [input() for i in range(N)]
ans = 0

# 시작점
for i in range(N):
    for j in range(M):
        if gold_map[i][j] == 'L':
            ans = max(ans, bfs(i, j))

print(ans)
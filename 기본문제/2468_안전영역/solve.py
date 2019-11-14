# bfs
'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

5
'''
def is_safe(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True

def bfs(x, y, t):
    q = []
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.pop(0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x + dx
            ny = y + dy
            if is_safe(nx, ny):
                if not visited[nx][ny] and area[nx][ny] > t:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


N = int(input())

area = [list(map(int, input().split())) for i in range(N)]
top = max(sum(area, []))
res = 1

for t in range(1, top):
    visited = [[0] * N for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > t:
                bfs(i, j, t)
                cnt += 1
    res = max(res, cnt)

print(res)
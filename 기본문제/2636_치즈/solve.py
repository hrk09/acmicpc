'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
​
3
5
'''

def is_safe(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True

# 외부공기 처리(처음 만난 0 을 bfs 돌리면서 모두 2로 돌림)
def out_air(x, y):
    q = []
    q.append((x, y))
    mat[x][y] = 2
    while q:
        x, y = q.pop(0)
        for (dx, dy) in d:
            nx, ny = x + dx, y + dy
            if is_safe(nx, ny):
                if mat[nx][ny] == 0:
                    mat[nx][ny] = 2
                    q.append((nx, ny))

# c면 처리(3), 치즈 내부(4)
def c_area(x, y):
    q = []
    q.append((x, y))
    mat[x][y] = 3
    while q:
        x, y = q.pop(0)
        for (dx, dy) in d:
            nx, ny = x + dx, y + dy
            if mat[nx][ny] == 1:
                mat[nx][ny] = 4  # 내부 처리
                if mat[nx + 1][ny] == 2 or mat[nx - 1][ny] == 2 or mat[nx][ny + 1] == 2 or mat[nx][ny - 1] == 2:
                    mat[nx][ny] = 3
                q.append((nx, ny))

# 치즈 녹이는 작업
def melt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                mat[i][j] = 0
            elif mat[i][j] == 3:
                mat[i][j] = 0
                cnt += 1
            elif mat[i][j] == 4:
                mat[i][j] = 1
    return cnt
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for h in range(n)]
cnt = 0

# 방향(상하좌우)
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while True:
    cnt += 1
    out_air(0, 0)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                c_area(i, j)
    last_one = melt()
    if not sum(sum(mat, [])):
        break
print(cnt)
print(last_one)
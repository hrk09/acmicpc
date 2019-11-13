import sys
sys.stdin = open('input.txt', 'r')
# 최소거리 == bfs

def is_safe(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True

def bfs(x, y):
    global min_dis
    q.append((x, y))
    visited.append((x, y))
    dis_arr[x][y] = 1
    while q:
        (x, y) = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_safe(nx, ny) and arr[nx][ny] == '1' and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.append((nx, ny))
                dis_arr[nx][ny] += dis_arr[x][y] + 1
    return dis_arr[n-1][m-1]

n, m = map(int, input().split())
arr = [input() for i in range(n)]
q = []
visited = []
dis_arr = [[0]*m for _ in range(n)]
min_dis = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
print(bfs(0, 0))

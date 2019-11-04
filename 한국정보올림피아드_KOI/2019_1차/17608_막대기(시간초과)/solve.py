'''
6
6
9
7
6
4
6

3

5
5
4
3
2
1

5
'''
# 시간초과
import sys

n = int(sys.stdin.readline())
sticks = [int(sys.stdin.readline()) for i in range(n)]
cnt = 0
view = set()

for i in range(n):
    m = max(sticks)
    s = sticks.pop(0)
    if s > m:
        cnt += 1
    if s == m:
        if s not in view:
            cnt += 1
            view.add(s)
print(cnt)
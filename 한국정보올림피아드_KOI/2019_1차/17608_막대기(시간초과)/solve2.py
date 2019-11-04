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
# 또간초과
n = int(input())
sticks = [int(input()) for i in range(n)]
cnt = 0
view = []
max_idx = sticks.index(max(sticks))

for i in range(max_idx, n):
    if sticks[i] == max(sticks[i:]) and sticks[i] not in view:
        cnt += 1
        view.append(sticks[i])
print(cnt)
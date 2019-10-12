scores = []
for i in range(1, 9):
    s = int(input())
    scores.append((s, i))
scores.sort()
final_scores = scores[-5:]
ans1 = 0
ans2 = []
for a, b in final_scores:
    ans1 += a
    ans2.append(b)
ans2.sort()
print(ans1)
print(' '.join([str(a) for a in ans2]))
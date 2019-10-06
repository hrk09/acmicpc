from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
res = 0
for card in combinations(cards, 3):
    # print(card) 조합이 튜플 형식으로 나옴
    if res < sum(card) <= m:
        # res 갱신작업(최대한 근접값에 나오도록)
        res = sum(card)
print(res)

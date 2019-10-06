# 분해합의 반대 프로세스인 생성자를 구하는 문제
'''
n 보다 작은 수를 다 조사하기 보다는 효율적인 for 문 범위조사
256 = 245 + 2 + 4 + 5
한자리는 최대 9의 수 가지니까 256 - 9 - 9 - 9 해서 229부터 255 조사
'''

'''
216

198
'''
n = int(input())
def solve(n):
    m = n-len(str(n))*9
    # 1보다 작으면 그냥 m은 1부터 조사함
    if m < 1: m = 1
    # 아니면, m부터 조사 가능
    else: m
    for i in range(m, n):
        s = i
        s += sum(map(int, str(i)))
        if s == n:
            return i
    return 0
print(solve(n))
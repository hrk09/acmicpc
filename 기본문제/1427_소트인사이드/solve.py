'''
2143
4321
'''
n = input()
n1 = []
for i in range(len(n)):
    n1 += [int(n[i])]
n1.sort()
n1.reverse()
print(''.join(str(i) for i in n1))
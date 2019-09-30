'''
4

9
'''
n = int(input())
bin_n = bin(n)[2:]
# print(bin_n)
res = 0

for i in range(len(bin_n)):
    res += (3 ** (len(bin_n)-i-1)) * int(bin_n[i])
print(res)






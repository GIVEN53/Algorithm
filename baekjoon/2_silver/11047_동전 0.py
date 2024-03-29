from sys import stdin

n, k = map(int, stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(n)]

cnt = 0
for coin in coins[::-1]:
    cnt += k // coin
    k %= coin

print(cnt)

##########################
#    memory: 31256KB     #
#    time:   44ms        #
##########################

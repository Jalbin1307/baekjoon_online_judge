N = int(input())
rest = 1000 - N
coins = [500, 100, 50, 10, 5, 1]
count = 0
for coin in coins:
    count += rest // coin
    rest = rest % coin

print(count)
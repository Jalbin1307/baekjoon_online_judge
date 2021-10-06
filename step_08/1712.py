A, B, C = map(int, input().split())
profit = C - B
if profit <= 0:
    print(-1)
else:
    print(A//profit + 1)
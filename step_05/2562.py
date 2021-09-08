max = 0
for i in range(9):
    N = int(input())
    if max < N:
        m = i
        max = N
print(max)
print(m+1)
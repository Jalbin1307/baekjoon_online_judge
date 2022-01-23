N, K = map(int,input().split())
A = []
t = 0
coin = 0
for i in range(N):
    A.append(int(input()))
    if A[i] <= K:
        t = i

for i in range(t,-1,-1):
    if K >= A[i]:
        c = A[i]
        coin += K // c
        K = K % c

print(coin)


N = int(input())
p = list(map(int, input().split()))
p.sort()
time = 0
for i in range(N):
    time += sum(p[:i+1])

print(time)
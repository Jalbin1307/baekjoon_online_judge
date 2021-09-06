N = int(input())
M = N
num = 0

def plus_cycle(N):
    a = N//10
    b = N%10
    c = (a + b) % 10
    M = b*10 + c
    return M

while True:
    M = plus_cycle(M)
    if M == N:
        print(num+1)
        break
    else:
        num += 1
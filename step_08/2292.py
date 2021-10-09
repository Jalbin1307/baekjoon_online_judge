N = int(input())
t = 1
start = 2
end = 7
while True:
    if N == 1:
        print(1)
        break
    if start <= N and N <= end:
            print(t+1)
            break
    else:
        start = start + 6 * t
        end = end + 6 * (t+1)
        t = t + 1
H, M = map(int, input().split())
check = 0
if M - 45 < 0:
    check = 1
    M = M + 15
else:
    M = M - 45
    
if check == 1:
    if  H == 0:
        H = 24
    H = H - 1

print("{} {}".format(H, M))
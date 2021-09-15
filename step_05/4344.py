def check_score(x, avg):
    if x > avg:
        return 1
    else:
        return 0

C = int(input())

for i in range(C):
    case = list(map(int, input().split()))
    avg = sum(case[1:])/case[0]
    count = sum(check_score(x, avg) for x in case[1:])
    print("{:.3f}%".format(count / (len(case)-1) * 100))
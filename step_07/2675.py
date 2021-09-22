def s_loop(R,S):
    result = ""
    for i in range(len(S)):
        result += S[i]*int(R)
    return result
    
N = int(input())
for i in range(N):
    R, S = input().split()
    print(s_loop(R,S))
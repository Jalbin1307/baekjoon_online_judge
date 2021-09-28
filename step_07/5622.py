S = input()
time = 0
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ','+-*/=']
for i in range(len(S)):
    for j in range(len(dial)):
        if S[i] in dial[j]:
            time += j+1
print(time+len(S)*2)
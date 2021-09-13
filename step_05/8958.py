def ox_score(ox):
    s = 1
    score = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            score = score + s
            s = s + 1
        elif ox[i] == 'X':
            s = 1 
    
    return score

N = int(input())
for i in range(N):
    ox = input()
    print(ox_score(ox))

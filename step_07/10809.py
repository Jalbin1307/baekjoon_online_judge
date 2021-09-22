S = input()
loc = {chr(i):-1 for i in range(97,123)}
for i in range(len(S)):
    if loc[S[i]] == -1:
        loc[S[i]] = i
    
for key in sorted(loc.keys()):
    print(loc[key], end=" ")
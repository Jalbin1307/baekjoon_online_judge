S = input()
S = S.upper()
max,chk = 0, -1
c =''
dic = {chr(i) : int(0) for i in range(65,91)}

for i in range(len(S)):
    dic[S[i]] += 1

for i in dic.keys():
    if dic[i] >= max:
        if dic[i] == max:
            chk = 1
        else:
            chk = 0
        max = dic[i]
        c = i

if chk == 1:
    print("?")
elif chk == 0:
    print(c)
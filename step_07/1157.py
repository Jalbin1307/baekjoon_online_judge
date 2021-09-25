S = input().upper()
dic = {chr(i) : 0 for i in range(65,91)}

for key in dic.keys():
    dic[key] = S.count(key)

val = list(dic.values())
val.sort(reverse=True)

if val[0]==val[1]:
    print("?")
else:
    for key in dic.keys():
        if dic[key] == val[0]:
            print(key)
            break
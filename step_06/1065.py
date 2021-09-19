def han(x):
    x = str(x)
    if len(x)<=2:
        return True
    else:
        for i in range(len(x)-2):
            if int(x[i+1])-int(x[i]) != int(x[i+2])-int(x[i+1]):
                return False
        return True


X = int(input())
result = 0
for i in range(1,X+1):
    if han(i):
        result += 1

print(result)

def self_number(n):
    result = n
    for i in str(n):
        result += int(i)
    return result

l = []
for i in range(1,10001):
    l.append(self_number(i))

for i in range(1, 10001):
    if i not in l:
        print(i)
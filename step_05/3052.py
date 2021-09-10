result = []
for i in range(10):
    N = int(input())
    result.append(N%42)
print(len(set(result)))
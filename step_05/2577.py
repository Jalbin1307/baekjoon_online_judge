A, B, C = map(int, (input(), input(), input()))

result = str(A*B*C)

for i in range(10):
    print(result.count(str(i)))
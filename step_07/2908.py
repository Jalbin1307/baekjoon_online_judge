A, B = input().split()
A = list(A)
B = list(B)
A.reverse()
B.reverse()
A = "".join(A)
B = "".join(B)
if A > B:
    print(A)
else:
    print(B)
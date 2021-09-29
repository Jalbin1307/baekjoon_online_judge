S = input()
length = len(S)
length -= S.count('c=')
length -= S.count('c-')
length -= S.count('dz=')*2
length -= S.count('d-')
length -= S.count('lj')
length -= S.count('nj')
length -= S.count('s=')
if S.count('dz=')>0:
    length = length - S.count('z=') + S.count('dz=')
else:
    length -= S.count('z=')
print(length)
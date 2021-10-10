X = int(input())
line = 0
max = 0
while X > max:
    line += 1
    max += line    
gap = max - X
top = line - gap
under = gap + 1
if line % 2 == 0:
    print(f'{top}/{under}')
else:
    print(f'{under}/{top}')
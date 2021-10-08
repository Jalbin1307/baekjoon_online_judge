def group(word):
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                return False
    return True
cnt = 0
N = int(input())
for i in range(N):
    word = input()
    if group(word) == True:
        cnt += 1

print(cnt)
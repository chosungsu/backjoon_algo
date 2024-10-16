n = 5
lines= []
length = [] # 입력받는 단어 각각의 길이를 나타내는 length 

for _ in range(n):
    word = input()
    length.append(len(word))
    lines.append(word)

ans = ''

for j in range(max(length)):
    for i in range(n):
        if j < length[i]:
            ans+=lines[i][j]

print(ans)
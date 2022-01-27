num = int(input())
for i in range(num):
    num_sec, s = input().split()
    text = ''
    for i in s:
        text += int(num_sec) * i
    print(text)
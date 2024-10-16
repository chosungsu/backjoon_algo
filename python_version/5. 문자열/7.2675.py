num = int(input())
for i in range(num):
    num_cnt, string = input().split()
    text = ''
    for s in string:
        text += int(num_cnt) * s
    print(text)
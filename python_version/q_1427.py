n = int(input())
li = []
for i in str(n):
    li.append(int(i))
#내림차순 정렬
li.sort(reverse=True)
for i in li:
    print(i,end='')
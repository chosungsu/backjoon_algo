list = []
for _ in range(5):
    list.append(int(input()))
list.sort()
print(int(sum(list)/5))
print(list[2])
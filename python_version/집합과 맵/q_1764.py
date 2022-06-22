n, m = list(map(int, input().split()))
set_hear = set()
for i in range(n) :
    set_hear.add(input())
set_see = set()
for i in range(m) :
    set_see.add(input())
result = sorted(list(set_hear&set_see))
print(len(result))
for name in result :
    print(name)
n, k = map(int, input().split())
scorelist = list(map(int,input().split()))
scorelist.sort(reverse=True)
print(scorelist[k - 1])
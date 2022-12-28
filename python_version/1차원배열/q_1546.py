n = int(input())
new_list = []
test_list = list(map(int, input().split()))
max_score = max(test_list)
for score in test_list :
    new_list.append(score/max_score *100)
test_avg = sum(new_list)/n
print(test_avg)
words = input().upper()
#중복값 제거
unique_words = list(set(words))
cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)
#최댓값이 중복되면 ?출력
if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])
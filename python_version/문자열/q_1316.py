a = int(input())
group = 0
for i in range(a) :
    word = input()
    error = 0
    for index in range(len(word) - 1) :
        #연속적인 문자가 아닐 경우
        #다음 인덱스부터의 문자열로 교체
        if word[index] != word[index + 1] :
            new_word = word[index + 1:]
            if new_word.count(word[index]) > 0 :
                error += 1
    if error == 0 :
        group += 1
print(group)
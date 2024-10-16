word1 = ' ' + input()
word2 = ' ' + input()

# 두 문자열의 부분 수열 중 긴 부분을 구하는 방법
# 두 문자열 중 word1을 기준으로 dp를 계산하자.

dp = [[0] * len(word2) for _ in range(len(word1))]
for i in range(1, len(word1)):
    for j in range(1, len(word2)):
        if word1[i] == word2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
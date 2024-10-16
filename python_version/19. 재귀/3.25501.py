import sys
def recursion(string, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif string[l] != string[r]: return 0
    else: return recursion(string, l+1, r-1)
def isPalindrome(string):
    return recursion(string, 0, len(string)-1)
t = int(sys.stdin.readline())
for _ in range(t):
    string = sys.stdin.readline().rstrip()
    cnt = 0
    print(isPalindrome(string), cnt)
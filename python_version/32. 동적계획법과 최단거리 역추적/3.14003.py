import sys

input=sys.stdin.readline
lenA=int(input())
data=list(map(int,input().split()))

dp=[[0,0]] # index도 저장
tracking=[0 for _ in range(lenA+1)]
idx=0

def binarySearch():
    global dp, tracking, idx
    
    for i in range(len(data)):
        target = data[i]
        if len(dp)==1 or dp[-1][0] < target :

            tracking[i] = dp[-1][1]
            dp.append([target,i])
            idx = i
            
        else:
            start,end = 0, len(dp)
            
            while end-start>1:
                
                mid = (start+end)//2      
                if dp[mid][0] >= target :
                    ans = mid
                    end=mid
                else:
                    start=mid
        
            dp[ans][0]=target
            dp[ans][1]=i
            tracking[i] = dp[ans-1][1]

binarySearch()

# 역추적
last_idx = len(dp) - 1
sol = []
for _ in range(len(dp)-1):
    sol.append(data[idx])
    idx = tracking[idx] 
sol.reverse()
print(last_idx)
print(*sol)
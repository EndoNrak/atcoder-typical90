N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def judge(x):
    cnt = 0
    now = 0
    for a in A+[L]:
        if a >= now+x:
            now = a
            cnt += 1
            if cnt == K+1:
                return True
    return False


min_ = 0
max_ = 10**9

while max_-min_ > 1:
    mid = (max_ + min_) // 2
    if judge(mid):
        min_ = mid
    else:
        max_ = mid
print(min_)
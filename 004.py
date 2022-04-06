H, W = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(H)]

H_sum = [sum([A[i][j] for i in range(H)]) for j in range(W)]
W_sum = [sum(A[i]) for i in range(H)]

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(H_sum[j]+W_sum[i]-A[i][j])
    print(*ans)
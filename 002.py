N = int(input())
ans = []
def rec(s, n, m):
    if n+m==N:
        ans.append(s)
        return
    if n < N//2:
        rec(s+"(", n+1, m)
    if n > m:
        rec(s+")", n, m+1)

if N%2 == 1:
    exit()

else:
    rec("(", 1, 0)
    for x in ans:
        print(x)

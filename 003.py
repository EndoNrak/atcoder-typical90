from collections import defaultdict, deque
N = int(input())
edges = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

def get_farest_point(start):
    q = deque()
    dist = [0]*N
    q.append(start)
    next_ = 0
    while q:
        p = q.popleft()
        for v in edges[p]:
            if dist[v] == 0 and v != start:
                dist[v] = dist[p] + 1
                q.append(v)
                next_ = v
    return next_, dist[next_]

v1, dv = get_farest_point(0)
_, dv2 = get_farest_point(v1)
print(dv2+1)